|contributions welcome| |Open Source Love| |MIT Licence|

.. raw:: html

   <h1 align="center">

.. raw:: html

    <img src="https://github.com/coderick14/ACedIt/blob/master/images/logo.png" width="500"/><br/>

.. raw:: html

   </h1>

A command line tool to run your code against sample test cases. Without leaving the terminal :)

Demo
^^^^

.. figure:: https://github.com/coderick14/ACedIt/blob/master/images/demo.gif
   :alt: Simple demo of how ACedIt works

Supported sites
^^^^^^^^^^^^^^^

-  Codeforces
-  Codechef
-  Spoj
-  Hackerrank

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

    usage: acedit [-h] [-s SITE] [-c CONTEST] [-p PROBLEM] [-f]
                  [--run SOURCE_FILE]
                  [--set-default-site {codeforces,codechef,hackerrank,spoj}]
                  [--set-workdir WORKDIR]

    optional arguments:
      -h, --help            show this help message and exit
      -s SITE, --site SITE  The competitive programming platform, e.g. codeforces,
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
      --set-workdir WORKDIR
                            ABSOLUTE PATH to working directory

During installation, the default site is set to ``codeforces`` and the
default working directory is set to ``/home/your-username/ACedIt``. You
can change them anytime using the above mentioned flags.

ACedIt requires the following working directory structure
**(Recommended)**. It also has the added advantage of keeping your work
organized :)

::

    workdir
       |
       |-ACedIt
       |   |
       |   |- Site1
       |   |    |- Contest1
       |   |    |     |- Problem1
       |   |    |     |- Problem2
       |   |    |- Contest2
       |   |    |     |- Problem1
       |   |    |     |- Problem2
       |   |- Site2
       |   |    |- Contest1
       |   |    |     |- Problem1

| During installation, ACedIt will set up the basic working directory structure.
| While prefetching test cases, it will modify the same accordingly without any user intervention.

But in case you’re writing your code in some other directory, you can use ``acedit --run <SOURCE_FILE> -s SITE -c CONTEST -p PROBLEM``. You can omit ``-s`` as it’ll take the default site.

But there’s no need to specify the ``-s``, ``-c`` and ``-p`` flags if you follow the above mentioned directory structure (ACedIt will create most of it for you on the fly :)


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

-  Test your code against sample cases (when following the recommended directory structure)

   ::

       acedit --run D.cpp

   ::

       acedit --run CHEFFA.py

-  Test your code against sample cases (from any other directory)

   ::

       acedit --run solve.cpp -c 835 -p D

   ::

       acedit --run test.py -s codechef -c AUG17 -p CHEFFA

Note :
''''''

There might be some issues with Spoj, as they have widely varying DOM trees for different problems. Feel free to contribute on this. Or anything else that you can come up with :)

.. |contributions welcome| image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
   :target: https://github.com/coderick14/ACedIt/issues
.. |Open Source Love| image:: https://badges.frapsoft.com/os/v2/open-source.svg?v=103
   :target: https://github.com/coderick14/ACedIt/
.. |MIT Licence| image:: https://badges.frapsoft.com/os/mit/mit.svg?v=103
   :target: https://opensource.org/licenses/mit-license.php