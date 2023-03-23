#!/usr/bin/env python
import setuptools
from tokenize_output import __version__

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='tokenize-output',
    version=__version__,
    license='BSD',
    author='anki-code',
    author_email='author@example.com',
    description="Get identifiers, names, paths, URLs and words from the command output.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=[
        'demjson3'
    ],
    extras_require={
        "dev": ["pytest"],
    },
    packages=setuptools.find_packages(),
    package_data={'tokenize_output': ['*.py']},
    scripts=['tokenize-output'],
    platforms='any',
    url='https://github.com/anki-code/tokenize-output',
    project_urls={
        "Documentation": "https://github.com/anki-code/tokenize-output/blob/master/README.md",
        "Code": "https://github.com/anki-code/tokenize-output",
        "Issue tracker": "https://github.com/anki-code/tokenize-output/issues",
    },
    classifiers=[
        'Programming Language :: Python'
    ]
)
