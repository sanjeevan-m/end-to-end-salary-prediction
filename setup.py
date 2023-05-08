from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements_packages(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file path.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()

    # Remove the '-e .' entry if present
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='salary_prediction_project',
    version='0.0.1',
    author='sanjeevan',
    author_email='sanjeevanwarrior@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements_packages('requirements.txt')
)
