from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='FanTree',
    version='0.2.0',    
    description='A module about decision tree',
    url='https://github.com/fanfansmilkyway/Decision-Tree',
    author='ShiYuan Fan',
    author_email='fanfansmilkyway@gmail.com',
    license='BSD 2-clause',
    packages=['trees'],
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)