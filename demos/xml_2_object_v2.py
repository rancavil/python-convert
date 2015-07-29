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

class Band(object):
	name = str
	genre = str

class Album(object):
	name = str
	year = int

class Music(object):
	Band = Band
	Albums = [Album]

doc = """
<Music>
	<Band>
		<name>Herbie Hancock</name>
		<genre>Jazz</genre>
	</Band>
	<Albums>
		<Album>
			<name>HeadHunters</name>
			<year>1973</year>
		</Album>
		<Album>
			<name>Sextant</name>
			<year>1973</year>
		</Album>
	</Albums>
</Music>
"""
if __name__ == '__main__':
	xml = parseString(doc)
	c = convertXML2OBJ(Music,xml.documentElement)

	print("XML original")
	print("************")
	print(xml.toxml())
	print("")
	print("Python OBJ")
	print("*************")
	print("Band                    ")
	print("------------------------")
	print("Name  : %s"%c.Band.name)
	print("Genre : %s"%c.Band.genre)
	print("")
	print("Albums                  ")
	print("------------------------")
	for a in c.Albums:
		print("\tAlbum name : %s"%a.name)
		print("\tYear       : %d"%a.year)
		print("")
