# coding: utf-8

import os
from setuptools import setup, find_packages  # noqa: H301

with open(
    os.path.join(os.path.dirname(__file__), "requirements.txt"), "r"
) as fh:
    requirements = fh.readlines()

NAME = "binance-py"
VERSION = "0.1.0"
PYTHON_REQUIRES = ">= 3.8"

setup(
    name=NAME,
    version=VERSION,
    description="Python client for Binance API",
    author="OpenXAPI",
    author_email="contact@openxapi.com",
    url="https://github.com/openxapi/binance-py",
    keywords=["OpenAPI", "binance", "binance-python"],
    install_requires=[req for req in requirements if req.strip()],
    packages=find_packages(exclude=["*.test"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description="""\
    Python client for Binance API
    """,  # noqa: E501
    package_data={"binance-py": ["py.typed"]},
)
