from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function returns a list of required packages
    '''
    HYPHEN_E_DOT='-e .'
    requirements=[]
    with open(file_path)as file:
        requirements=file.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    
    return requirements
    

setup(
name="ML Project",
version="0.0.1",
author="pradyumn",
author_emails="pradybisht@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)