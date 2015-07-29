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

doc = {'sender' : { 'userid' : 1220000, 'username' : 'Fred '}, 'receiver' : { 'userid' : 203201, 'username' : 'Kathy' } , "num" : 1, "text" : 'Hey please send me the mail'}

class User(object):
	userid = int
	username = str

class Message(object):
	num = int
	text = str
	sender = User
	receiver = User

c = convertJSON2OBJ(Message,doc)
print("JSON original")
print("*************")
print(json.dumps(doc, sort_keys=True, indent=2, separators=(',',': ')))
print("")
print("Python obj     ")
print("***************")
print("Message        ")
print("---------------")
print("num  : %d "%c.num)
print("text : %s "%c.text)
print("")
print("Sender         ")
print("---------------")
print("c.sender.userid   : %d "%c.sender.userid)
print("c.sender.username : %s "%c.sender.username)
print("Receiver       ")
print("---------------")
print("c.receiver.userid   : %d "%c.receiver.userid)
print("c.receiver.username : %s "%c.receiver.username)
print("")
