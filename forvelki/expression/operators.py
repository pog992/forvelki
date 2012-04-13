#!/usr/bin/env python
# -*- coding: utf-8 -*-

class add(object):
	def __init__(self, v1, v2):
		self.v1 = v1
		self.v2 = v2
		
	def __repr__(self):
		return "{0} + {1}".format(self.v1, self.v2)
	
class subtract(object):
	def __init__(self, v1, v2):
		self.v1 = v1
		self.v2 = v2
		
	def __repr__(self):
		return "{0} - {1}".format(self.v1, self.v2)

class multiply(object):
	def __init__(self, v1, v2):
		self.v1 = v1
		self.v2 = v2
		
	def __repr__(self):
		return "{0} * {1}".format(self.v1, self.v2)
	
class divide(object):
	def __init__(self, v1, v2):
		self.v1 = v1
		self.v2 = v2
		
	def __repr__(self):
		return "{0} / {1}".format(self.v1, self.v2)
	
class negate(object):
	def __init__(self, value):
		self.value = value
		
	def __repr__(self):
		return "!({0})".format(self.value)