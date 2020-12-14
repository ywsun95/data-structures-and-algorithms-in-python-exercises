import subprocess
import sys
import os

if __name__ == '__main__':
    dir_path = os.path.realpath(os.path.dirname(__file__))
    subprocess.Popen([sys.executable, os.path.join(dir_path, '2.9-2.15.py')]).wait()
