# PD Archive Extractor

This repo contains a shell and python script for the `pd-extract-archive` command. This is a Linux command to extract Proactive Disclosure records from archive `tar.gz` files for a specific PD type and Organization.

## Requirements

- Python3
- `click` installed for Python3 on a root or user level:
    - `python3 -m pip install click`
    - `python3 -m pip install --user click`

## Installation

1. Pull the repo into any directory
1. Add that directory into your `PATH` variable

## Examples

```
pd-extract-archive --type=grants --org=tbs-sct --input=./my-archive.tar.gz --output=./grants.csv
```