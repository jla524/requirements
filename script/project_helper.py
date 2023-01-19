import sys
import subprocess as sp


def run_tests():
    try:
        sp.run('pytest --capture=tee-sys', check=True, shell=True)
    except sp.CalledProcessError as error:
        print(str(error))
        sys.exit(1)
