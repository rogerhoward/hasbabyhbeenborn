import os, sys

PROJECT_DIR = '/var/www/hasbabyhbeenborn'

activate_this = os.path.join('/home/rogerhoward/.virtualenvs/hasbabyhbeenborn/bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from server import app as application