from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('VERSION') as f:
    version = f.read()

prj_name = "my-project"
prj_folder = prj_name.replace('-', '_')

setup(
    name=prj_name,
    version=version,
    description="template",
    keywords=["keyword"],
    url="",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=required,
    scripts=[
        prj_folder + "/bin/script.py"
    ],
)