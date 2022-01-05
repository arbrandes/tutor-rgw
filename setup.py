#!/usr/bin/env python

import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="tutor-s3",
    use_scm_version=True,
    url="https://github.com/hastexo/tutor-contrib-s3/",
    project_urls={
        "Code": "https://github.com/hastexo/tutor-contrib-s3",
        "Issue tracker": "https://github.com/hastexo/tutor-contrib-s3/issues",
    },
    license="AGPLv3",
    author='hastexo',
    author_email='pypi@hastexo.com',
    description="A Tutor plugin for storage via an S3-compatible service",
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor"],
    setup_requires=["setuptools-scm"],
    entry_points={"tutor.plugin.v0": ["s3 = tutors3.plugin"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
