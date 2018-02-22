[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/coderick14/ACedIt/issues)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/coderick14/ACedIt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<h1 align="center">
    <img src="https://github.com/coderick14/ACedIt/blob/master/images/logo.png" width="500"/><br/>
</h1>
A command line tool to run your code against sample test cases. Without leaving the terminal :) 

#### Demo
![ACedIt demo GIF](https://github.com/coderick14/ACedIt/blob/master/images/demo.gif "Simple demo of how ACedIt works" )  

#### Supported sites
+ AtCoder
+ Codeforces (including gyms)
+ Codechef
+ Spoj
+ Hackerrank

#### Supported Languages
+ C
+ C++
+ Python
+ Java
+ Ruby
+ Haskell

#### Requirements
+ python3.5
+ coreutils (macOS only)

#### Installation
+ `git clone https://github.com/kotapiku/ACedIt`
+ `cd ACedIt`
+ `python setup.py install`


#### Usage
```
usage: acedit [-h] [-s {codeforces,codechef,hackerrank,spoj}] [-c CONTEST]
              [-p PROBLEM] [-f] [--run SOURCE_FILE]
              [--set-default-site {codeforces,codechef,hackerrank,spoj}]
              [--set-default-contest DEFAULT_CONTEST] [--clear-cache]

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

```
During installation, the default site is set to `AtCoder`. You can change it anytime using the above mentioned flags.  

#### Examples
+ Fetch test cases for a single problem  
```
acedit -s atcoder -c abc088 -p a
```
+ Fetch test cases for all problems in a contest  
```
acedit -s atcoder -c abc088
```
+ Force download test cases, even when they are cached  
```
acedit -s atcoder -c abc088 -p a -f
```
+ Test your code (when default-site and default-contest is set and filename is same as problem_code)
```
acedit --set-default-contest abc088 // set contest
acedit  // fetch data
acedit --run a.cpp
```
**Since your filename is same as problem code, there's no need for the `-p` flag.**
+ Test your code (specifying contest and problem codes explicitly)
```
acedit --run d.cpp -c abc084 -p d
```
```
acedit --run test.py -s codechef -c AUG17 -p CHEFFA
```

##### Note :
+ The working directory structure mentioned in the previous versions is no longer required and supported.

+ There might be some issues with Spoj, as they have widely varying DOM trees for different problems. Feel free to contribute on this. Or anything else that you can come up with :)

##### Contributors
+ [Lakshmanaram](https://github.com/lakshmanaram)
+ [Igor Kolobov](https://github.com/Igorjan94)
