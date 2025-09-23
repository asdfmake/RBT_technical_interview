from setuptools import setup, find_packages

setup(
    name="rbt_technical_interview",
    version="0.1",
    packages=find_packages(include=["app", "app.*"]),
)
