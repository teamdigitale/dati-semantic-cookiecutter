import setuptools

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="dati_playground",
    description="Tools to check semantic assets",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    include_package_data=True,
    package_data={"": ["data/*.yaml"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)