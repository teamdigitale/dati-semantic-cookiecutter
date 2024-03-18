import setuptools

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="dati_semantic_cookiecutter",
    version="0.1.0",
    description="Tools to check semantic assets",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    include_package_data=True,
    package_data={"": ["scripts/*.py"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)