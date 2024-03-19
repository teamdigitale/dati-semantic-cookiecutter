from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="dati_semantic_cookiecutter",
    version="0.1.0",
    description="Tools to check semantic assets",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
    packages=find_packages('.'),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "check_repo_structure = scripts.check_repo_structure:main",
        ]
    },
#    include_package_data=True,
#    package_data={"": ["scripts/*.py"]},
)