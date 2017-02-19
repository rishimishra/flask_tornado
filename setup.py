"""A setuptools based setup module"""
from setuptools import setup, find_packages
from codecs import open # To use a consistent encoding
from os import path

current_path = path.abspath(path.dirname(__file__))

# Can read description from README.rst
with open(path.join(current_path, 'README.rst'), encoding='utf-8') as f:
	project_description = f.read()

# Calling global setup function
setup(
	name='lflask',
	version='1.0.0',
	description='Learning how to integrate kerberos and tornado with Flask',
	long_description=project_description,
	url='git url here',
	author='Rishi Mishra',
	author_email='rishi.x.mishra@gmail.com',
	license='Free for use',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Web Servers',
		'License :: Free for use',
		'Programming Language :: Python :: 2.7',
	],
	keywords='flask tornado kerberos integration sample',
	packages=find_packages(exclude=['tests']),
	install_requires=['flask', 'tornado'],
	extras_require={
		'dev': ['check-manifest'],
		'test': ['coverage'],
	},
	# package_data
	# data_files
	# entry_points
	test_suite='nose.collector',
	tests_require=['nose'],

	)