from setuptools import setup, find_packages

setup(
    name='hello_publish',
    version='0.1.0',
    packages=find_packages(include=['hello_publish', 'hello_publish.*'])
)