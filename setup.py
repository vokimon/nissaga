#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from nissaga import __version__, __doc__

readme = open("README.md").read()

setup(
	name = "nissaga",
	version = __version__,
	description = __doc__,
	author = "David García Garzón",
	author_email = "voki@canvoki.net",
	url = 'https://github.com/vokimon/nissaga',
	long_description = readme,
	long_description_content_type = 'text/markdown', 
	license = 'GNU Affero General Public License v3 or later (AGPLv3+)',
	packages=find_packages(exclude=['*[tT]est*']),
    entry_points = {
        'console_scripts': [
            'nissaga=nissaga.cli:main',
        ],
    },
	install_requires=open('requirements.txt').read().splitlines(),
	include_package_data = True,
	test_suite = 'nissaga',
	classifiers = [
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
        'Topic :: Sociology :: Genealogy',
		'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Operating System :: OS Independent',
	],
)


# vim: et sw=4 ts=4
