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

import inspect
import json
from xml.dom.minidom import parseString

def check_type(a):
	if isinstance(a,int):
		return True
	elif isinstance(a,float):
		return True
	elif isinstance(a,str):
		return True

def convert(class_to_convert,type_to_convert):
	filter_attr = filter(lambda a: a not in dir(object) and inspect.ismethod(getattr(class_to_convert,a)) == False and a not in ("__doc__", "__module__","__dict__","__weakref__"),dir(class_to_convert))

	data = None
	class_name = class_to_convert.__class__.__name__	

	if type_to_convert == "xml":
		data = "<"+class_name+">"
		for v in filter_attr:
			d = getattr(class_to_convert,v)
			if type(d).__name__ == "instance":
				data += convert(d,type_to_convert)
			elif isinstance(d,list):
				data += "<"+v+"s>"
				for a in d:
					if not check_type(a):
						data += convert(a,type_to_convert)
					elif check_type(a):
						data += "<"+v+">"+str(a)+"</"+v+">"
				data += "</"+v+"s>"
			else:
				data += "<"+v+">"
				data += str(d)
				data += "</"+v+">"

		data += "</"+class_name+">"
		return data

	elif type_to_convert == "json":
		data = dict()
		for v in filter_attr:
			d = getattr(class_to_convert,v)
			if type(d).__name__ == "instance":
				data[v] = convert(d,type_to_convert)
			elif isinstance(d,list):
				list_of_element = list()
				for a in d:
					if not check_type(a):
						list_of_element.append(convert(a,type_to_convert))
					elif check_type(a):
						list_of_element.append(a)

					data[v+"s"] = list_of_element
			else:
				data[v] = d

		return data

def convert2XML(class_to_convert):
	data = convert(class_to_convert,"xml")
	return parseString(data)

def convert2JSON(class_to_convert):
	data = convert(class_to_convert,"json")
	return json.loads(json.dumps(data))