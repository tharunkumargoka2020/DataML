from setuptools import setup, find_packages

# Project metadata
NAME = 'dataml'
DESCRIPTION = 'DataML is a data science and machine learning library for Python'
VERSION = '0.1.0'
AUTHOR = 'DataML'
EMAIL = 'dataml.gtk@gmail.com'

# Required packages
REQUIRED_PACKAGES = [
    'setuptools',
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(exclude=['tests']),  # Auto-discover packages
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Data Science & ML'
    ],
)
