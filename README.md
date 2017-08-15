[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/coderick14/ACedIt/issues)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/coderick14/ACedIt/) 
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
<h1 align="center">
    <img src="https://github.com/coderick14/ACedIt/blob/master/images/logo.png" width="500"/><br/>
</h1>
A command line tool to run your code against sample test cases. Without leaving the terminal :) 

#### Installation
##### Build from source
+ `git clone https://github.com/coderick14/ACedIt`
+ `cd ACedIt`
+ `python setup.py install`

##### As a Python package
```
sudo pip install ACedIt
```

#### Usage
```
usage: ACedIt [-h] [-s SITE] [-c CONTEST] [-p PROBLEM] [-f]
              [--run SOURCE_FILE]

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

```

ACedIt requires the following working directory structure.
```
root-dir
   |
   |- Site1
   |    |- Contest1
   |    |     |- Problem1
   |    |     |- Problem2
   |    |- Contest2
   |    |     |- Problem1
   |    |     |- Problem2
   |- Site2
   |    |- Contest1
   |    |     |- Problem1

```
During installation, ACedIt will set up the basic working directory structure.  
While prefetching test cases, it will modify the same accordingly without any user intervention.  
But in case you're writing your code first and then using `ACedIt --run <source_file>`, make sure you follow the directory structure mentioned.

#### Supported sites
+ Codeforces
+ Codechef
+ Spoj
+ Hackerrank

#### Examples
+ Fetch test cases for a single problem  
```
ACedIt -s codechef -c AUG17 -p CHEFFA
```
+ Fetch test cases for all problems in a contest  
```
ACedIt -s codechef -c AUG17
```
+ Force download test cases, even when they are cached  
```
ACedIt -s codeforces -c 86 -p D -f
```
+ Test your code against sample cases  
```
ACedIt --run D.cpp
```
```
ACedIt --run CHEFFA.py
```

#### Demo
![ACedIt demo GIF](https://github.com/coderick14/ACedIt/blob/master/images/demo.gif "Simple demo of how ACedIt works" )

##### Note : 
There might be some issues with Spoj, as they have widely varying DOM trees for different problems. Feel free to contribute on this. Or anything else that you can come up with :)
