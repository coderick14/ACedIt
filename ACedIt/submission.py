import json
import re
import os
import util
import threading
import progressbar
import sys
try:
    from bs4 import BeautifulSoup as bs
    import requests as rq
    import grequests as grq
    from argparse import ArgumentParser
except:
    err = """
    You haven't installed the required dependencies.
    Run 'python setup.py install' to install the dependencies.
    """
    print err
    sys.exit(0)


class Utilities:

    cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "ACedIt")

    @staticmethod
    def store_code(site, contest, contestant, problem_code, code):
        """
        Utility function to store code
        """
        directory = os.path.join(
            os.getcwd(), site, contest + "_submissions", contestant)

        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.join(
            os.getcwd(), site, contest + "_submissions", contestant, problem_code)

        with open(filename, 'w') as handler:
            try:
                handler.write(code.encode('utf-8'))
            except:
                print "Failed to get " + contestant + "'s code for " + problem_code

    @staticmethod
    def download_submission(args):
        if args["site"] == "codeforces":
            platform = Codeforces(args)
        platform.get_all_submissions()

    @staticmethod
    def get_html(url):
        """
        Utility function get the html content of an url
        """
        try:
            r = rq.get(url)
        except Exception as e:
            sys.exit(0)
        return r

    @staticmethod
    def empty_pool(pool):
        """
        Utility function to join all threads in pool
        """
        for thread in pool:
            thread.join()
        return []

    @staticmethod
    def set_found_code(found_code):
        """
        Utility function to create map for problem codes
        """
        for key, value in found_code.items():
            found_code[key] = False
        return found_code

    @staticmethod
    def update_status(pbar, status_flag, status_lock):
        """
        Utility function to update status bar while threading
        """
        status_lock.acquire(True)
        pbar.update(status_flag["previous"] + status_flag["increment"])
        status_flag["previous"] += status_flag["increment"]
        status_lock.release()


class Codeforces(util.Codeforces):
    """
    Class to handle downloading of test cases from Codeforces
    """

    def __init__(self, args):
        self.site = args["site"]
        self.contest = args["contest"]
        self.problem = args["problem"]
        self.nos = 0
        if args["submission"].isdigit():
            self.nos = int(args["submission"])
        else:
            self.user = args["submission"]

    def get_rank_list(self):
        """
        Method to get the rank list of the contest
        """
        url = "http://codeforces.com/contest/" + self.contest + "/standings"
        res = Utilities.get_html(url)
        soup = bs(res.text, "html.parser")
        rankList = []
        currentCount = 1

        for link in soup.find_all("a"):
            link = str(link.get("href"))
            try:
                match = re.search("/profile/(.*)", link).group(1)
                rankList.append(match)
                currentCount += 1
                if currentCount > self.nos:
                    break
            except Exception as e:
                continue

        return rankList

    def get_code(self, submission_id):
        """
        Method to get the code for submission id of a contestant
        """
        url = "http://codeforces.com/contest/" + \
            self.contest + "/submission/" + submission_id
        res = Utilities.get_html(url)
        soup = bs(res.text, 'lxml')
        return soup.pre.string

    def get_all_pages(self, url, contestant):
        """
        Method to get the entire history of submission pages by the contestant
        """
        res = Utilities.get_html(url)
        soup = bs(res.text, 'lxml')
        span_set = soup.findAll("span", {"class": "page-index"})
        maxPageCount = 1

        if len(span_set) is not 0:
            span = span_set[-1]
            maxPageCount = re.search('/page/(.*?)"', str(span)).group(1)
            maxPageCount = int(maxPageCount)

        url = "http://codeforces.com/submissions/" + contestant + "/page/"
        maxPageCount += 1
        pageLinks = []

        for page_no in range(1, maxPageCount):
            pageLinks.append(url + str(page_no))

        responses = (grq.get(link) for link in pageLinks)
        pages = grq.map(responses)

        return pages

    def get_valid_submissions(self, contestant, page, count, found_code):
        """
        Method to get all the submissions that match the problem and contest code
        """

        return found_code

    def get_user_submission(self, contestant, found_code, pbar, status_lock, status_flag, single_user):
        url = "http://codeforces.com/submissions/" + contestant
        pages = self.get_all_pages(url, contestant)
        submissions_found = False
        count = len(found_code)
        found_users_code = False

        for page in pages:
            prevcount = count

            if count is 0 or page is None:
                return

            soup = bs(page.text, "lxml")
            tr_set = soup.find_all("tr")

            for tr in tr_set:
                contest_details_res = re.search(
                    'href="/problemset/problem/(.*?)"', str(tr))
                problem_status_res = re.search(
                    'submissionverdict="(.*?)"', str(tr))
                submission_id_res = re.search('submissionid="(.*?)"', str(tr))

                if contest_details_res and problem_status_res and submission_id_res:
                    contest_details = contest_details_res.group(1).split('/')
                    contest_code = contest_details[0]
                    pcode = contest_details[1]
                    problem_status = problem_status_res.group(1)
                    submission_id = submission_id_res.group(1)
                    filename = os.path.join(
                        os.getcwd(), "codeforces", self.contest + "_submissions", contestant, pcode)

                    if os.path.exists(filename):
                        found_users_code = True
                        continue

                    if problem_status == "OK":
                        problem_status = "AC"

                    if contest_code == self.contest and found_code[pcode] == False and problem_status == "AC":
                        try:
                            AC_code = self.get_code(submission_id)
                        except Exception as e:
                            continue
                        Utilities.store_code(
                            "codeforces", self.contest, contestant, pcode, AC_code)
                        found_code[pcode] = True
                        count -= 1

                        if single_user:
                            Utilities.update_status(
                                pbar, status_flag, status_lock)
                        found_users_code = True

        if not single_user:
            Utilities.update_status(pbar, status_flag, status_lock)

    def get_all_submissions(self):
        url = "http://codeforces.com/contest/" + self.contest
        req = Utilities.get_html(url)

        try:
            problem_links = self.get_problem_links(req)
        except Exception as e:
            print "Couldn't find submissions for the contest you were looking for"
            return

        found_code = {}

        for link in problem_links:
            pcode_res = re.search('problem/(.*)', link)
            if pcode_res is not None:
                pcode = pcode_res.group(1)
                found_code[pcode] = False
            else:
                return

        status_flag = {"previous": 0, "increment": 1}
        status_lock = threading.Lock()

        if self.nos is not 0:
            print "Fetching submissions"

            try:
                rankList = self.get_rank_list()
            except Exception as e:
                print "Couldn't find submissions for the contest you were looking for, Try again later"
                return

            rankListCount = len(rankList)
            pbar = progressbar.ProgressBar(max_value=rankListCount)
            pool = []

            for contestant in rankList:
                found_code_copy = found_code.copy()
                thread = threading.Thread(target=self.get_user_submission, args=(
                    contestant, found_code_copy, pbar, status_lock, status_flag, False,))
                thread.start()
                pool.append(thread)

                if len(pool) > 10:
                    pool = Utilities.empty_pool(pool)
        else:
            pbar = progressbar.ProgressBar(max_value=len(found_code))
            print "Fetching " + self.user + "'s submissions"
            self.get_user_submission(
                self.user, found_code, pbar, status_lock, status_flag, True)
