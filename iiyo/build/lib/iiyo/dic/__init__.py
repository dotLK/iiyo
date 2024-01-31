from __future__ import unicode_literals
from .db import *


def word(word: object):
    return db.dic[word]
