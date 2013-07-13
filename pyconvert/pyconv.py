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

def check_type(obj):
	""" function check the data types 
		parameter: obj, object to checking 
		return: True or False
	"""
	if isinstance(obj,int):
		return True
	elif isinstance(obj,float):
		return True
	elif isinstance(obj,long):
		return True
	elif isinstance(obj,str):
		return True

def convertOBJ2STR(class_to_convert,type_to_convert):
	""" function to convert an python object in a str or dict (with a representation of xml or json)
		parameters:
			class_to_convert, a python object to convert in a str
			type_to_convert, a string with "xml" o "json" 
		returns:
			if type_to_convert is equals to "xml" convert the object in a str with xml xml_document
			if type_to_convert is equals to "json" convert the object in a dictionary with json document						
	"""
	filter_attr = filter(lambda a: a not in dir(object) and inspect.ismethod(getattr(class_to_convert,a)) == False and a not in ("__doc__", "__module__","__dict__","__weakref__"),dir(class_to_convert))

	data = None
	class_name = class_to_convert.__class__.__name__	

	if type_to_convert == "xml":
		data = "<"+class_name+">"
		for v in filter_attr:
			d = getattr(class_to_convert,v)
			if type(d).__name__ == "instance":
				data += convertOBJ2STR(d,type_to_convert)
			elif isinstance(d,list):
				data += "<"+v+"s>"
				for a in d:
					if not check_type(a):
						data += convertOBJ2STR(a,type_to_convert)
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
				data[v] = convertOBJ2STR(d,type_to_convert)
			elif isinstance(d,list):
				list_of_element = list()
				for a in d:
					if not check_type(a):
						list_of_element.append(convertOBJ2STR(a,type_to_convert))
					elif check_type(a):
						list_of_element.append(a)

					data[v+"s"] = list_of_element
			else:
				data[v] = d

		return data

def convert2XML(class_to_convert):
	""" function to convert an python object in a xml document
		parameters:  
			class_to_convert, a python object to convert in a xml document
		returns:
			xml.dom.minidom.Document						
	"""
	data = convertOBJ2STR(class_to_convert,"xml")
	return parseString(data)

def convert2JSON(class_to_convert):
	""" function to convert an python object in a json document (dict)
		parameters:  
			class_to_convert, a python object to convert in a json document (python dictionary)
		returns:
			dict						
	"""
	data = convertOBJ2STR(class_to_convert,"json")
	return json.loads(json.dumps(data))

def convertJSON2STR(name_doc, json_doc):
	""" function to convert a python dict in a string (str) with the representation of xml document
		parameters:  
			name_doc, element root for the document
			json_doc, a dictionary (dict) with the json document
		returns:
			str
	"""
	xml_doc = ""
	if isinstance(json_doc,list):
		xml_doc += "<"+name_doc+"s>"
		for element in json_doc:
			xml_doc += convertJSON2STR(name_doc,element)
		xml_doc += "</"+name_doc+"s>"
		return xml_doc

	xml_doc = "<"+name_doc+">"
	for key in json_doc.keys():
		value = json_doc[key]
		if isinstance(value,dict):
			xml_doc += convertJSON2STR(key,value)
		elif isinstance(value,list):
			xml_doc += "<"+key+"s>"
			for v in value:
				if isinstance(v,dict):
					xml_doc += convertJSON2STR(key,v)
				else:
					xml_doc += "<"+key+">"+str(v)+"</"+key+">"
			xml_doc += "</"+key+"s>"
		else:
			xml_doc += "<"+key+">"+str(value)+"</"+key+">"

	xml_doc += "</"+name_doc+">"

	return xml_doc

def convertJSON2XML(name_doc, json_doc):
	""" function to convert a python dict in a xml documento (xml.dom.minidom.Document)
		parameters:  
			name_doc, element root for the document
			json_doc, a dictionary (dict) with the json document
		returns:
			xml.dom.minidom.Document
	"""
	xml_document = convertJSON2STR(name_doc, json_doc)
	return parseString(xml_document)