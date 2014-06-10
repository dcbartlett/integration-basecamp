from setuptools import setup

PACKAGE = 'TracHelloworld'
VERSION = '0.1'

setup(
	name=PACKAGE,
    version=VERSION,
    packages=['helloworld'],
    entry_points={'trac.plugins': '%s = helloworld' % PACKAGE},
)