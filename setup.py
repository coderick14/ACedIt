try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
import json
import os

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

default_site = 'codeforces'
workdir = os.path.join(os.path.expanduser('~'), 'ACedIt')
cache_dir = os.path.join(os.path.expanduser('~'), '.cache', 'ACedIt')

from ACedIt.main import supported_sites

for site in supported_sites:
	# create cache directory and working directory structure
    if not os.path.isdir(os.path.join(cache_dir, site)):
        os.makedirs(os.path.join(cache_dir, site))
    if not os.path.isdir(os.path.join(workdir, site)):
    	os.makedirs(os.path.join(workdir, site))

data = {'default_site': default_site.strip(), 'workdir': os.path.expanduser('~'),
        'cachedir': cache_dir}
with open(os.path.join(cache_dir, 'constants.json'), 'w') as f:
    f.write(json.dumps(data, indent=2))

setup(
    name='ACedIt',

    packages=['ACedIt'],

    version='1.0.1',

    description='Download and test against sample test cases from any competitive programming website',

    author='Deep Bhattacharyya',

    author_email='bhattacharyya.rick14@gmail.com',

    install_requires=requirements,

    entry_points={
        'console_scripts': ['ACedIt=ACedIt.main:main']
    },

    zip_safe=False,

    url='https://github.com/coderick14/ACedIt',

    keywords=['sample test cases', 'downloader', 'competitive programming'],

    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Education',
    ],

    license='MIT License'
)
