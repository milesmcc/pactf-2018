from os.path import abspath, dirname, join


#  TODO(Yatharth): Actually use this in places
PROJECT_NAME = 'pactf'

ENVDIR_PATH = join(dirname(abspath(__file__)), 'envdir')
DJANGO_DIR = dirname(dirname(abspath(__file__)))
BASE_DIR = dirname(DJANGO_DIR)