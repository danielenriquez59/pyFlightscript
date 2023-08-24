from setuptools import setup, find_packages

setup(
    name="pyFlightscript",
    version="0.1.0",
    description="Python package to write FlightStream scripts using python.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Daniel Enriquez",
    author_email="daniel.enriquez@researchinflight.com",
    url="https://github.com/xxxx",
    packages=find_packages(),  # automatically discover and include all packages in the package directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3.0",  # Modified license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
    ],
    extras_require={
        # additional dependencies for development
    },
    package_data={
        # include data files with the package
    },
)

# Add the copyright statement
print("Copyright © 2023 Research In Flight")  # replace YEAR with the current year or the year of copyright
