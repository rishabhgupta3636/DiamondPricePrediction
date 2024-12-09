from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]
        requirements.append(requirement)
    
    return requirements



setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='RishabhGupta',
    author_email='gupta.rishabh98@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


# One way is this to run the setup.py file and make package
# Another way is to write -e . in the requirement.txt file and run -> pip install -r requirement.txt but ensure to
# handle this in the install_requires parameter because it will try to install this package and fail because no such 
# package exists so handle like if requirment!='-e .' then append else no append