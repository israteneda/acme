from setuptools import setup, find_packages

from acme import __version__

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="acme-exercise",
    version=__version__,
    description="Console app to calculate the total that the company has to pay an employee.",
    license="MIT",
    author="Israel Teneda",
    author_email="israteneda@gmail.com",
    url="https://github.com/israteneda/acme",
    packages=find_packages(),
    package_data={'acme': ['data/employees.txt']},
    entry_points={
        "console_scripts": [
            "acme=acme.__main__:main"
        ]
    },
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.7",
    project_urls={
        "Homepage": "https://github.com/israteneda/acme",
        "Source Code": "https://github.com/israteneda/acme",
    },
)
