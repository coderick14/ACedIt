import sys
import util


supported_sites = ["codeforces", "codechef", "hackerrank", "spoj"]


def validate_args(args):
    if args["site"] not in supported_sites:
        print "Sorry. ACedIt only supports %s till now." % (", ".join(supported_sites))
        sys.exit(0)
    if not args["site"] == "spoj" and args["contest"] is None:
        print "Please specify a contest code"
        sys.exit(0)


def main():
    args = util.parse_flags()
    validate_args(args)

    if args["problem"] is not None:
        # fetch single problem
        util.scrape_problem(args)
    else:
        # fetch all problems for the contest
        print "Fetch all"

    print args


if __name__ == "__main__":
    main()
