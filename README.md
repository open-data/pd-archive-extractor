# PD Archive Extractor

This repo contains a python module script for the `pd-extract-archive` command. This is a Python command to extract Proactive Disclosure records from archive `tar.gz` files for a specific PD type and Organization.


## Installation

1. Pull the repo into any directory:
    - `git clone https://github.com/open-data/pd-archive-extractor.git`
1. Navigate into the directory, and install the module via pip:
    - `cd pd-archive-extractor; pip install -e ./; pip install -r requirements.txt;`

## Examples

```
pd-extract-archive --type=grants --org=tbs-sct --input=./my-archive.tar.gz --output=./grants.csv
```