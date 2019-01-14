import setuptools
from pyconsole_util import util

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="Console Utilities",
    version="0.0.1",
    author="Gatlen Culp",
    author_email="gatlenculp@gmail.com",
    description="A set of functions that print to the console in different formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github something",
    packages=setuptools.find_packages()
)
