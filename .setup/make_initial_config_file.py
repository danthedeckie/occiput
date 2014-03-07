# This very simple script generates a simple config.py file, including
# a brand new temporary SECRET_KEY, which is a random number, dumped through
# sha512 twice.  That will probably do for now, but you are advised to change
# it to something application specific, and as incredibly hard to guess as
# possible.  Of course. :-)
#
# TODO:
# - app name?

from hashlib import sha512
from random import random

x=sha512()
x.update(str(random()))
x.update(x.hexdigest())

print ('''
#AUTOGENERATED! You should be changing this stuff.
from config_default import *
SECRET_KEY='{0}' #TODO - you should change this!
'''.format(x.hexdigest()))