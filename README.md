# Requirements

Install [poetry][1] dependencies with [pip][2].


## Quickstart Guide
1. Clone this repository
   ```
   git clone git@github.com:jla524/requirements.git
   cd requirements
   ```
   
2. Create a virtual environment (optional)
   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the required dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run the conversion script
   ```
   python3 requirements/convert.py <path to project>
   ```
   To generate requirements without version specifiers
   ```
   python3 requirements/convert.py <path to project> --noversion
   ```


[1]: https://python-poetry.org
[2]: https://pip.pypa.io/en/stable/
