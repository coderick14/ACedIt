import sys, json, re
try:
    from bs4 import BeautifulSoup as bs
    import requests as rq
    from argparse import ArgumentParser
except:
    err = """
    You haven't installed the required dependencies.
    Run 'python setup.py install' to install the dependencies.
    """
    print err
    sys.exit(0)

def parse_flags():
    parser = ArgumentParser()

    parser.add_argument("-s", "--site",
                        dest="site",
                        help="The competitive programming platform, e.g. codeforces, codechef etc")

    parser.add_argument("-c", "--contest",
                        dest="contest",
                        help="The name of the contest, e.g. JUNE17, LTIME49, COOK83 etc")

    parser.add_argument("-p", "--problem",
                        dest="problem",
                        help="The problem code, e.g. OAK, PRMQ etc")

    args = parser.parse_args()

    flags = {}

    if args.site is None:
        import json
        default_site = None
        try:
            with open("constants.json", "r") as f:
                data = f.read()
            data = json.loads(data)
            default_site = data.get("default_site", None)
        except:
            pass

        flags["site"] = default_site
    else:
        flags["site"] = args.site

    flags["contest"] = args.contest
    flags["problem"] = args.problem

    flags["site"] = flags["site"].lower()

    return flags

def scrape_problem(args):

	def codeforces():
		print "Fetching problem " + args["contest"] + "-" + args["problem"] + " from Codeforces..."

		url = "http://codeforces.com/contest/" + args["contest"] + "/problem/" + args["problem"]
		r = rq.get(url)
		soup = bs(r.text, "html.parser")

		inputs = soup.findAll("div", {"class" : "input"})
		outputs = soup.findAll("div", {"class" : "output"})
		
		repls = ("<br>","\n"), ("<br/>","\n"), ("</br>","")

		formatted_inputs, formatted_outputs = [], []

		for inp in inputs:
			pre = inp.find("pre").decode_contents()
			pre = reduce(lambda a, kv : a.replace(*kv), repls, pre)
			formatted_inputs += [pre]

		for out in outputs:
			pre = out.find("pre").decode_contents()
			pre = reduce(lambda a, kv : a.replace(*kv), repls, pre)
			formatted_outputs += [pre]

		print "Inputs", formatted_inputs
		print "Outputs", formatted_outputs

	def codechef():
		print "Fetching problem " + args["contest"] + "-" + args["problem"] + " from Codechef..."

		url = "https://codechef.com/api/contests/" + args["contest"] + "/problems/" + args["problem"]
		r = rq.get(url)
		data = json.loads(r.text)
		soup = bs(data["body"], "html.parser")

		test_cases = soup.findAll("pre")
		formatted_inputs, formatted_outputs = [], []

		input_list = [
			"<pre>(.|\n)*<b>Input:?</b>:?",
			"<b>Output:?</b>(.|\n)+</pre>"
		]

		output_list = [
			"<pre>(.|\n)+<b>Output:?</b>:?",
			"</pre>"
		]

		input_regex = re.compile("(%s)" % "|".join(input_list))
		output_regex = re.compile("(%s)" % "|".join(output_list))

		for case in test_cases:
			inp = input_regex.sub("", str(case))
			out = output_regex.sub("", str(case))

			formatted_inputs += [inp.strip()]
			formatted_outputs += [out.strip()]

		print "Inputs", formatted_inputs
		print "Outputs", formatted_outputs

	def spoj():
		print "Fetching problem " + args["problem"] + " from SPOJ..."

		url = "http://spoj.com/problems/" + args["problem"]
		r = rq.get(url)
		soup = bs(r.text, "html.parser")

		test_cases = soup.findAll("pre")
		formatted_inputs, formatted_outputs = [], []

		input_list = [
			"<pre>(.|\n|\r)*<b>Input:?</b>:?",
			"<b>Output:?</b>(.|\n|\r)*"
		]

		output_list = [
			"<pre>(.|\n|\r)*<b>Output:?</b>:?",
			"</pre>"
		]

		input_regex = re.compile("(%s)" % "|".join(input_list))
		output_regex = re.compile("(%s)" % "|".join(output_list))

		for case in test_cases:
			inp = input_regex.sub("", str(case))
			out = output_regex.sub("", str(case))

			formatted_inputs += [inp.strip()]
			formatted_outputs += [out.strip()]

		print "Inputs", formatted_inputs
		print "Outputs", formatted_outputs

	eval(args["site"] + "()")