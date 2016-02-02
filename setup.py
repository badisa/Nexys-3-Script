from setuptools import setup

setup(
    name='Nexys-UFC-Script',
    version="0.0.1",
    description="A script for creating UFC files for Nexys 3 Boards",
    long_description=open("README.rst").read(),
    url="https://github.com/badisa/Nexys-3-Script/",
    author="Forrest York",
    author_email="forrest.york@gmail.com",
    license="MIT",
    scripts=[
        "ufc_generator.py"
    ],
    zip_safe=False
)
