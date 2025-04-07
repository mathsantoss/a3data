import os
from pathlib import Path

from setuptools import find_packages, setup

from _version import __version__


requirements_files = ["requirements.txt"]
requirements_path = join(dirname(realpath(__file__)), "requirements")
setup_path = Path(__file__).parent

requirements = []

for file_name in requirements_files:
    with open(join(requirements_path, file_name), "r") as f:
        requirements.append(f.readlines())

setup(
    name="a3data",
    version=__version__,
    description="Iris Model API",
    url="Git Hub Project URL",
    maintainer="",
    maintainer_email="",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[],
    install_requires=requirements,
    extras_require={},
    python_requires=">=3.10",
    classifiers=["Programming Language :: Python :: 3.10"],
)
