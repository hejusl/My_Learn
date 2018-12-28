# !/usr/local/bin/python3
# coding=utf-8

from learning.withBoy.base import value
from learning.withBoy.b import hello


print('scope base', value, id(value))
value = 20
print('scope local', value, id(value))
hello()
