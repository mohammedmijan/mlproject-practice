from setuptools import setup, find_packages
from typing import List

HYPEN_DOT = 'e- .'

def get_requirements(file_path:str) -> List[str]:
    """
    It is a requirement file
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements

setup(
    name="Mizan MLProject", 
    version="0.0.1",
    author="Mizan", 
    author_email="mejan601@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)