from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List(str):
    '''
    will return something
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
ame='end e end ml project-1',
version='0.0.1',
author='deepak',
author_emails='deepakkpasi@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)