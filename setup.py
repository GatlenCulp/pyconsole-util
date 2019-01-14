import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pyconsole-util",
    version="1.0.1",

    author="Gatlen Culp",
    author_email="gatlenculp@gmail.com",
    description="A set of functions that print to the console in different formats for debugging, exploring, or printing nicely",
    keywords="console printing colors formatting format debug info explorer",
    license="GPLv3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/Hugernot/pyconsole-util",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Debuggers"
    ]
)
