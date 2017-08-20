import sys
import util


supported_sites = ['codeforces', 'codechef', 'hackerrank', 'spoj']


def validate_args(args):
    """
    Method to check valid combination of flags
    """

    if args['default_site'] is not None or args['default_contest'] is not None:
        return

    if args['clear_cache']:
        return

    if not args['site'] == 'spoj' and args['contest'] is None:
        print 'Please specify contest code or set a default contest.'
        sys.exit(0)

    if args['source']:
        return

    if args['site'] == 'spoj' and args['problem'] is None:
        print 'Please specify a problem code for Spoj.'
        sys.exit(0)


def main():
    args = util.Utilities.parse_flags(supported_sites)
    validate_args(args)

    try:
        if args['default_site']:
            # set default site
            util.Utilities.set_constants('default_site', args['default_site'])

        elif args['default_contest']:
            # set default contest
            util.Utilities.set_constants('default_contest', args['default_contest'])

        elif args['clear_cache']:
            # clear cached test cases
            util.Utilities.clear_cache(args['site'])

        elif args['source']:
            # run code
            util.Utilities.run_solution(args)

        elif args['problem'] is not None:
            # fetch single problem
            util.Utilities.download_problem_testcases(args)

        elif args['contest']:
            # fetch all problems for the contest
            util.Utilities.download_contest_testcases(args)

        else:
            print 'Invalid combination of flags.'

    except KeyboardInterrupt:
        # Clean up files here
        util.Utilities.handle_kbd_interrupt(
            args['site'], args['contest'], args['problem'])


if __name__ == '__main__':
    main()
