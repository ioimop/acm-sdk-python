from setuptools import setup, find_packages
import aioacm


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aioacm-sdk-python",
    version=aioacm.__version__,
    packages=find_packages(exclude=["test"]),
    url="https://github.com/imopio/aioacm-sdk-python",
    license="Apache License 2.0",
    author="acm",
    author_email="755063194@qq.com",
    description="Python client for ACM with asyncio support.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["aiohttp", ""],
    entry_points={
      "console_scripts": ["acm=acm.command:main"],
    },
)
