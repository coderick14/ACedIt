import sys
import util


supported_sites = ['codeforces', 'codechef', 'hackerrank', 'spoj']


def validate_args(args):

    if args['default_site'] is not None or args['workdir'] is not None:
        return

    if args['source']:
        # Check if all flags have been specfied explicitly
        if (args['site'] == 'spoj' or args['contest']) and args['problem']:
            return

        # If at least one is specified (but not all), it's not a valid
        # combination
        if args['site'] or args['contest'] or args['problem']:
            print 'ACedIt requires site, contest(not required for SPOJ) and problem explicitly in case workdir structure is not followed.'
            sys.exit(0)

        # No flags specified, so take arguments from path
        return

    if not args['site'] == 'spoj' and args['contest'] is None:
        print 'Please specify a contest code.'
        sys.exit(0)

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

        if args['workdir']:
            # set working directory
            util.Utilities.set_constants(
                'workdir', args['workdir'], supported_sites)

        elif args['source']:
            # run code
            util.Utilities.run_solution(args)

        elif args['problem'] is not None:
            # fetch single problem
            util.Utilities.download_problem_testcases(args)

        elif args['contest']:
            # fetch all problems for the contest
            util.Utilities.download_contest_testcases(args)

    except KeyboardInterrupt:
        # Clean up files here
        util.Utilities.handle_kbd_interrupt(
            args['site'], args['contest'], args['problem'])


if __name__ == '__main__':
    main()
