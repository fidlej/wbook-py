
import os.path

BASE = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def apppath(*parts):
    return os.path.join(BASE, *parts)

