
from setuptools import setup, find_packages
setup(
    name="my_project",
    version="0.1",
    url="https://github.com/Keanmair/otus-qa-course",
    author="Semyon",
    author_email="keanmair@gmail.com",
    description="HomeWork",
    packages=find_packages(exclude=['otus-qa-course']),
    install_requires=['pytest>=4.6.4']
)