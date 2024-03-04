from setuptools import setup

setup(
    name='pd_archive_extractor',
    version='0.1.0',
    description='Python script to extract PD Records from archive files',
    url='https://github.com/open-data/pd-archive-extractor',
    author='Jesse Vickery',
    author_email='jesse.vickery@tbs-sct.gc.ca',
    license='MIT',
    packages=['pd_archive_extractor'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'pd-extract-archive = pd_archive_extractor.extract_archive:extract_rows',
        ],
    },
)
