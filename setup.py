"""
Source build and installation script.
"""

from os import path, sep, walk
from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages


def extract_requirements(filename):
    return [str(r.req) for r in parse_requirements(filename, session=PipSession)]


def find_package_data(source, strip=''):
    pkg_data = []
    for root, dirs, files in walk(source):
        pkg_data += map(
            lambda f: path.join(root.replace(strip, '').lstrip(sep), f),
            files
        )
    return pkg_data


base_dir = path.dirname(__file__)

with open(path.join(base_dir, 'README.rst')) as f:
    long_description = f.read()

install_requires = extract_requirements('requirements.txt')

setup(
    name='python-cafe-sqlalchemy',
    version='0.4.0',
    description='Handy SQLAlchemy bits and bobs, as an extension for Cafe',
    long_description=long_description,
    license='APLv2',
    url='https://github.com/betsybookwyrm/python-cafe-sqlalchemy',
    author='Elizabeth Alpert',
    author_email='lizbeth.alpert@gmail.com',
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    install_requires=install_requires,
)
