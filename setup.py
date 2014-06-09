from setuptools import find_packages, setup

setup(
    name='TracHelloWorld', version='1.0',
    packages=find_packages(exclude=['*.tests*']),
    entry_points = {
        'trac.plugins': [
            'helloworld = myplugs.helloworld',
        ],
    },
)
