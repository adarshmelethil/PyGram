#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="PyGram",
    version="0.1",
    description="Python interface to instagram",
    url="https://github.com/adarshmelethil/PyGram",
    download_url="",
    license="MIT",
    keywords=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    author="Adarsh Melethil",
    author_email="adarshmelethil@gmail.com",
    install_requires=["docopts"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["pygram=pygram.cli:main"]},
)
