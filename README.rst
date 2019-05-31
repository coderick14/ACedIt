A command line tool to run your code against sample test cases. Without leaving the terminal :)

Supported sites
^^^^^^^^^^^^^^^

-  Codeforces
-  Codechef
-  Spoj
-  Hackerrank
- Atcoder

Supported languages
^^^^^^^^^^^^^^^^^^^

-  C
-  C++
-  Python
-  Java
-  Ruby
-  Haskell

Installation
^^^^^^^^^^^^

Build from source
'''''''''''''''''

-  ``git clone https://github.com/coderick14/ACedIt``
-  ``cd ACedIt``
-  ``python setup.py install``

As a Python package
'''''''''''''''''''

::

    pip install --user ACedIt

Usage
^^^^^

::

    usage: acedit [-h] [-s {codeforces,codechef,hackerrank,spoj}] [-c CONTEST]
              [-p PROBLEM] [-f] [--run SOURCE_FILE]
              [--set-default-site {codeforces,codechef,hackerrank,spoj}]
              [--set-default-contest DEFAULT_CONTEST]

    optional arguments:
      -h, --help            show this help message and exit
      -s {codeforces,codechef,hackerrank,spoj}, --site {codeforces,codechef,hackerrank,spoj}
                            The competitive programming platform, e.g. codeforces,
                            codechef etc
      -c CONTEST, --contest CONTEST
                            The name of the contest, e.g. JUNE17, LTIME49, COOK83
                            etc
      -p PROBLEM, --problem PROBLEM
                            The problem code, e.g. OAK, PRMQ etc
      -f, --force           Force download the test cases, even if they are cached
      --run SOURCE_FILE     Name of source file to be run
      --set-default-site {codeforces,codechef,hackerrank,spoj}
                            Name of default site to be used when -s flag is not
                            specified
      --set-default-contest DEFAULT_CONTEST
                            Name of default contest to be used when -c flag is not
                            specified
      --clear-cache         Clear cached test cases for a given site. Takes
                            default site if -s flag is omitted

During installation, the default site is set to ``codeforces``. You
can change it anytime using the above mentioned flags.


Examples
^^^^^^^^

-  Fetch test cases for a single problem

   ::

       acedit -s codechef -c AUG17 -p CHEFFA

-  Fetch test cases for all problems in a contest

   ::

       acedit -s codechef -c AUG17

-  Force download test cases, even when they are cached

   ::

       acedit -s codeforces -c 86 -p D -f

-  Test your code (when default-site and default-contest is set and filename is same as problem_code)

   ::

       acedit --run D.cpp

   ::

       acedit --run CHEFFA.py

   **Since your filename is same as problem code, there's no need for the -p flag.**

-  Test your code (specifying contest and problem codes explicitly)

   ::

       acedit --run solve.cpp -c 835 -p D

   ::

       acedit --run test.py -s codechef -c AUG17 -p CHEFFA

Note :
''''''

-  The working directory structure mentioned in the previous versions is no longer required and supported.

-  There might be some issues with Spoj, as they have widely varying DOM trees for different problems. Feel free to contribute on this. Or anything else that you can come up with :)