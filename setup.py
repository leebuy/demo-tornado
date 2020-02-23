# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

install_requires = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt", "r") as f:
        for item in f.read().split("\n"):
            if item != "":
                install_requires.append(item)

setup(
    name="PyMicroChat3",
    version="0.1",
    packages=find_packages(),
    install_requires=install_requires,
    data_files=[("app", ["app/logging.yaml"])],
    author="inewbit",
    author_email="",
    description="pymicrochat3",
)
