from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements
    """
    requrements = []

    with open(file_path, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requrements 

setup(
    name="end-to-end-ml-project",
    version="0.0.1",
    author="Ilian Hadzhidimitrov",
    author_email="webmaster99@mail.bg",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)

