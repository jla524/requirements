# Requirements

Install [poetry][1] dependencies with [pip][2].

## Quickstart Guide

1. Clone this repository

   ```bash
   git clone git@github.com:jla524/requirements.git
   cd requirements
   ```

2. Run the conversion script

   ```bash
   python3 requirements/convert.py <path to project>
   ```

   To generate requirements without version specifiers

   ```bash
   python3 requirements/convert.py <path to project> --noversion
   ```


[1]: https://python-poetry.org
[2]: https://pip.pypa.io/en/stable/
