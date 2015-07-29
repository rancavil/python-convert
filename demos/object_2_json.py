#!/usr/bin/env python
#
# Copyright 2013 Rodrigo Ancavil del Pino
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# -*- coding: utf-8 -*-

import pyconvert.pyconv

""" This example convert an python object in a json document (python dictionary) """
class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	# Setters
	def setName(self, name):
		self.name = name
	def setAge(self, age):
		self.age = age
	# Getters
	def getName(self):
		return self.name
	def getAge(self):
		return self.age

person = Person("Steve",25)

print('')
print('Object python Person')
print('======================================')
print(' person = Person("Steve",25) ')
print(' person.name = %s'%person.getName())
print(' person.age  = %d'%person.getAge())
print('======================================')
print('')
print('JSON Document (python dictionary)     ')
print('======================================')
print('')
json_doc = pyconvert.pyconv.convert2JSON(person)
print(json_doc)
print('')
print('======================================')
