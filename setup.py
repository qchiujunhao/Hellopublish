from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class Install_with_sym(install):
    def run(self):
        install.run(self)
        path = os.getcwd()

setup(
    name='hello_publish',
    version='0.1.0',
    packages=find_packages(include=['hello_publish', 'hello_publish.*'])
)