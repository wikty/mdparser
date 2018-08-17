import os

class LoaderException(Exception):
    pass

def load(filename, encoding='utf8'):
    if not os.path.isfile(filename):
        raise LoaderException("file %s doesn't exists." % filename)
    lines = []
    with open(filename, 'r', encoding=encoding) as f:
        lines = f.readlines()
    