from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="COFFEE MASTER",
    version="0.1",
    author="Vaishnavi",
    packages=find_packages(),
    install_requires = requirements,
)