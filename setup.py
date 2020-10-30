# setup.py file

import setuptools 
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unit_3_sprint1", # the name that you will install via pip
    version="0.0.1",
    author="Elif Ayar",
    author_email="your@email.com",
    description="A collection of data science utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/ayarelif/unit_3_sprint1",
    #keywords="",
    packages=setuptools.find_packages(), # ["my_lambdata"]
    python_requires=">=3.9"
)