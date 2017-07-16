try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

import sys, json, os

with open("requirements.txt", "r") as f:
	requirements = [line.strip() for line in f.readlines()]

extra = {}
if sys.version_info >= (3,):
	extra["use_2to3"] = True

print "Please specify a default site (codeforces) :",
default_site = raw_input()
if default_site == "":
	print "Setting codeforces as default site"
	default_site = "codeforces"

print "Please specify working directory (relative to home directory) :",
workdir = raw_input()
if workdir == "":
	workdir = "ACedIt"
workdir = os.path.join(os.path.expanduser("~"), workdir)

if not os.path.isdir(workdir):
	os.makedirs(workdir)

print "Setting " + workdir + " as working directory"


data = {"default_site": default_site.strip(), "workdir" : workdir}
with open("constants.json", "w") as f:
    f.write(json.dumps(data))

setup(
	name = "ACedIt",

	packages = ["ACedIt"],

	version = "1.0",

	description = "Download and test against sample test cases from any competitive programming website",

	author = "https://github.com/coderick14",

	author_email = "bhattacharyya.rick14@gmail.com",

	install_requires = requirements,

	entry_points = {
		"console_scripts" : ["ACedIt=ACedIt.main:main"]
	},

	url = "https://github.com/coderick14/ACedIt",

	keywords = ["sample test cases", "downloader", "competitive programming"],

	classifiers = [
				"Operating System :: POSIX :: Linux",
                "License :: OSI Approved :: MIT License",
                "Programming Language :: Python :: 2.7",
				"Topic :: Education",
			],

	license = "MIT License"	
)
