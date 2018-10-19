#!/usr/bin/python
# -*- coding: utf-8 -*-

from xnntest import config as gl

name = gl.get_value('name')
score = gl.get_value('score')

print("%s: %s" % (name, score))
