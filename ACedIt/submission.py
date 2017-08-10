import json
import re
import os
import util
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
    def download_submission(args):
        if args["site"] == "codechef":
            platform = Codechef(args)
        
            platform.get_submission()

class Codechef:
    """
    Class to handle downloading of test cases from Codeforces
    """

    def __init__(self, args):
        self.site = args["site"]
        self.contest = args["contest"]
        self.problem = args["problem"]
        self.nos = int(args["submission"])
        self.status = args["status"]
        self.status_dict = {"AC":"15", "WA":"14", "TLE":"13", "RTE":"12", "CTE":"11"}
        if args["username"] is not None:
            self.username = args["username"]
        else:
            self.username = ""

    def get_submission(self):
        """
        Method to get submissions
        """

        print "Fetching submissions for " + self.contest + "-" + self.problem + " from Codechef..."
        status = self.status_dict[self.status]
        url = "https://www.codechef.com/"+ self.contest + "/status/" + self.problem + "?sort_by=Date%2FTime&sorting_order=asc&language=All&" "status=" + status + "&handle=" + self.username
        res = util.Utilities.get_html(url)
        soup = bs(res.text, 'html.parser')
        cnt = 1

        for link in soup.find_all('a'):
            link = str(link.get('href'))
            match = re.search(r'viewsolution',link)
            if match:
                print "https://codechef.com" + link
                cnt+=1
                if cnt > self.nos:
                    break

