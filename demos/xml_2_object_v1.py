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

from pyconvert.pyconv import convertXML2OBJ
from xml.dom.minidom import parseString

""" This example convert an xml document in a python object """

person_xml = "<Person>\
	         <name>Steve</name>\
                 <age>24</age>\
              </Person>"

class Person(object):
	name = str
	age = int

xml_doc = parseString(person_xml)

person_obj = convertXML2OBJ(Person, xml_doc)

print("XML original")
print("============")
print(xml_doc.toprettyxml())
print("")
print("Python object")
print("=============")
print("person_obj.name = %s"%person_obj.name)
print("person_obj.age  = %d"%person_obj.age)
