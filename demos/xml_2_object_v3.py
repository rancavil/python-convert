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

xmlDoc = """
      <Book>
         <isbn>0596001282</isbn>
         <language>English</language>
         <title>Python and XML</title>
         <authors>
              <author>Christopher A. Jones</author>
              <author>Fred L.Drake, Jr.</author>
         </authors>
         <url>http://www.amazon.com/Python-XML-Christopher-A-Jones/dp/0596001282</url>
      </Book>
"""

class Book(object):
	isbn = int
	language = str
	title = str
	authors = [str]
	url = str

xml = parseString(xmlDoc)
obj = convertXML2OBJ(Book,xml.documentElement)

print("XML original")
print("************")
print(xml.toxml())
print("")
print("Python Object")
print("*************")
print("isbn     : %ld "%obj.isbn)
print("language : %s  "%obj.language)
print("title    : %s  "%obj.title)
print("url      : %s  "%obj.url)
print("Authors")
for author in obj.authors:
	print("\t %s "%author)
	print("")
