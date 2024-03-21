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
            "check_filename_format = scripts.check_filename_format:main",
            "check_filename_match_uri = scripts.check_filename_match_uri:main",
            "check_filenames_match_directories = scripts.check_filenames_match_directories:main",
            "check_supported_files = scripts.check_supported_files:main",
            "check_versioning_pattern = scripts.check_versioning_pattern:main",
            "directory_existence_checker = scripts.directory_existence_checker:check_directory_existence"
        ]
    },
)
