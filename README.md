# PD Archive Extractor

This repo contains a python module script for the `pd-extract-archive` command. This is a Python command to extract Proactive Disclosure records from archive `tar.gz` files for a specific PD type and Organization.


## Installation

1. Pull the repo into any directory:
    - `git clone https://github.com/open-data/pd-archive-extractor.git`
1. (Optional) Create a python virtual environment:
    - `pd-archive-extractor`
    - `python3 -m venv pd_extract_venv`
    - `. pd_extract_venv/bin/activate`
1. Navigate into the directory, and install the module via pip:
    - `pip install -e . && pip install -r requirements.txt`
1. Confirm that the package is installed:
    - `which pd-extract-archive`

## Examples

```
pd-extract-archive --type=grants --org=tbs-sct --input=./my-archive.tar.gz --output=./grants.csv
```