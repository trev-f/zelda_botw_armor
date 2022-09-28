#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Trevor F. Freeman",
    author_email='trvrfreeman@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Zelda Breath of the Wild Armor Guide is a tool to track armor upgrades in Zelda Breath of the Wild.",
    entry_points={
        'console_scripts': [
            'zelda_botw_armor=zelda_botw_armor.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='zelda_botw_armor',
    name='zelda_botw_armor',
    packages=find_packages(include=['zelda_botw_armor', 'zelda_botw_armor.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/trev-f/zelda_botw_armor',
    version='v0.0.0',
    zip_safe=False,
)
