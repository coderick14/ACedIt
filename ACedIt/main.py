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
    if args["site"] == "spoj" and args["problem"] is None:
        print "Please specify a problem code for Spoj"
        sys.exit(0)


def main():
    args = util.Utilities.parse_flags()
    validate_args(args)
    try:
        if args["problem"] is not None:
            # fetch single problem
            util.Utilities.download_problem_testcases(args)
        else:
            # fetch all problems for the contest
            util.Utilities.download_contest_testcases(args)
    except KeyboardInterrupt:
        # Clean up files here
        print "Interruped manually. Exiting gracefully."

    print args


if __name__ == "__main__":
    main()
