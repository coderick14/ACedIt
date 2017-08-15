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

print 'Please specify a default site (codeforces) :',
default_site = raw_input()
if default_site == '':
    print 'Setting codeforces as default site'
    default_site = 'codeforces'

print 'Please specify working directory (relative to home directory) :',
workdir = raw_input()
if workdir == '':
    workdir = 'ACedIt'
workdir = os.path.join(os.path.expanduser('~'), workdir)

from ACedIt.main import supported_sites

if not os.path.isdir(workdir):
    os.makedirs(workdir)
    for site in supported_sites:
        os.makedirs(os.path.join(workdir, site))

cache_dir = os.path.join(os.path.expanduser('~'), '.cache', 'ACedIt')
if not os.path.isdir(cache_dir):
    os.makedirs(cache_dir)
    for site in supported_sites:
        os.makedirs(os.path.join(cache_dir, site))

print 'Setting ' + workdir + ' as working directory'


data = {'default_site': default_site.strip(), 'workdir': workdir,
        'cachedir': cache_dir}
with open(os.path.join(cache_dir, 'constants.json'), 'w') as f:
    f.write(json.dumps(data, indent=2))

setup(
    name='ACedIt',

    packages=['ACedIt'],

    version='1.0.0',

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
