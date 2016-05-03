'''
Created on Apr 29, 2016

@author: iitow
'''
from setuptools import setup, find_packages

SRCDIR = 'src'


def readme():
    ''' Spits out README.rst for our long_description
    with open('README.rst', 'r') as fobj:
        return fobj.read()
    '''


setup(
    name='pytomd',
    version='1.0.1',
    description="python code to README.md",
    long_description=readme(),
    author='ian.itow',
    author_email='ian.itow@isilon.com',
    url='',
    license='',
    classifiers=[
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
    ],
    package_dir={'': SRCDIR},
    packages=find_packages(SRCDIR),
    zip_safe=False,
    install_requires=[
        'requests==2.7.0',
        'PyYAML==3.10'
    ],
    entry_points={
        'console_scripts': ['pytomd = pytomd.__main__:main']
    },
    include_package_data=True,
)