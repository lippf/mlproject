from setuptools import setup, find_packages
import typing 

def get_requirements(filename:str)->list:
    '''
    Read a requirements file and return a list of requirements
    '''
    with open(filename, 'r') as f:
        return f.read().splitlines()



setup(
    name='my_package',
    version='0.0.1',
    author='Fergus Lipp',
    author_email='ferguslipp3@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
