try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

from acedit.install_entry import InstallEntry

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

with open('README.rst', 'rb') as f:
    long_description = f.read().decode('utf-8')

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name='ACedIt',

    packages=['acedit'],

    version='1.1.0',

    description='Download and test against sample test cases from any competitive programming website',

    long_description=long_description,

    author='Deep Bhattacharyya',

    author_email='bhattacharyya.rick14@gmail.com',

    install_requires=requirements,

    entry_points={
        'console_scripts': ['acedit=acedit.main:main']
    },

    zip_safe=False,

    url='https://github.com/coderick14/ACedIt',

    keywords=['sample test cases', 'downloader', 'competitive programming'],

    cmdclass={
            'install': InstallEntry,
            'develop': InstallEntry,
    },

    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Education',
    ],

    license='MIT License'
)
