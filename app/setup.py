from setuptools import find_packages, setup

with open("../requirements.txt", mode="r") as rf:
    install_requires = rf.readlines()

setup(
    name="ticket system",
    version="1.0",
    description="modern ticket system API",
    packages=find_packages(where="app"),
    install_requires=install_requires,
    python_requires=">=3.12",
)
