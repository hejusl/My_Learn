# !/usr/local/bin/python3
# coding=utf-8

from learning.withBoy import base


def hello():
    print('scope base', base.value, id(base.value))
