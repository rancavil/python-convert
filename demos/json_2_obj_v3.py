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

from pyconvert.pyconv import convertJSON2OBJ
import json

doc = [{'username' : 'fred', 'age' : 20} , {'username' : 'barney', 'age' : 20}] 

class User(object):
	username = str
	age = int

users = convertJSON2OBJ(User,doc)
print("JSON original")
print("*************")
print(json.dumps(doc, sort_keys=True, indent=2, separators=(',',': ')))
print("")
print("Python obj     ")
print("***************")
print("Users          ")
print("---------------")
for user in users:
	print("\tuser.username : %s "%user.username)
	print("\tuser.age      : %s "%user.age)
	print("")
