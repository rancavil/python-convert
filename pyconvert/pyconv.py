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

import sys

if sys.version_info > (3,):
	long = int
	unicode = str

class Encoder(json.JSONEncoder):
	""" class to handle ObjectId on a json document """
	def default(self,obj):
		try:
			from bson.objectid import ObjectId
		except ImportError:
			raise Exception("You must have bson installed")

		if isinstance(obj, ObjectId):
			return unicode(obj)
		else:
			return obj

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
	elif isinstance(obj,unicode):
		return True

def convert(class_to_convert,type_to_convert):
	""" function to convert an python object in a str or dict (with a representation of xml or json)
		parameters:
			class_to_convert, a python object to convert in a str or dict (python dictionary)
			type_to_convert, a string with "xml" o "json" 
		returns:
			if type_to_convert is equals to "xml" convert the object in a str with xml xml_document
			if type_to_convert is equals to "json" convert the object in a dictionary with json document						
	"""
	filter_attr = class_to_convert.__dict__
	data = None
	class_name = class_to_convert.__class__.__name__	

	if type_to_convert == "xml":
		data = "<"+class_name+">"
		for v in filter_attr:
			d = getattr(class_to_convert,v)
			if not check_type(d) and not isinstance(d,list):
				data += convert(d,type_to_convert)
			elif isinstance(d,list):
				data += "<"+v+"s>"
				for a in d:
					if not check_type(a):
						data += convert(a,type_to_convert)
					elif check_type(a):
						data += "<"+v+">"+unicode(a)+"</"+v+">"
				data += "</"+v+"s>"
			else:
				data += "<"+v+">"
				data += unicode(d)
				data += "</"+v+">"

		data += "</"+class_name+">"
		return data

	elif type_to_convert == "json":
		data = dict()
		for v in filter_attr:
			d = getattr(class_to_convert,v)
			if not check_type(d) and not isinstance(d,list):
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
	""" function to convert an python object in a xml document
		parameters:  
			class_to_convert, a python object to convert in a xml document
		returns:
			xml.dom.minidom.Document						
	"""
	data = convert(class_to_convert,"xml")
	return parseString(data)

def convert2JSON(class_to_convert):
	""" function to convert an python object in a json document (dict)
		parameters:  
			class_to_convert, a python object to convert in a json document (python dictionary)
		returns:
			dict						
	"""
	data = convert(class_to_convert,"json")
	return json.loads(json.dumps(data))

def convertJSON2STR(root_element, json_doc):
	""" function to convert a python dict in a string (str) with the representation of xml document
		parameters:  
			root_element, element root for the document
			json_doc, a dictionary (dict) with the json document
		returns:
			str
	"""
	xml_doc = ""
	if isinstance(json_doc,list):
		xml_doc += "<"+root_element+"s>\n"
		for element in json_doc:
			xml_doc += convertJSON2STR(root_element,element)
		xml_doc += "</"+root_element+"s>\n"
		return xml_doc

	xml_doc = "<"+root_element+">\n"
	for key in json_doc.keys():
		value = json_doc[key]
		if isinstance(value,dict):
			xml_doc += convertJSON2STR(key,value)
		elif isinstance(value,list):
			xml_doc += "<"+key+"s>\n"
			for v in value:
				if isinstance(v,dict):
					xml_doc += convertJSON2STR(key,v)
				else:
					xml_doc += "<"+key+">"+unicode(v)+"</"+key+">\n"
			xml_doc += "</"+key+"s>\n"
		else:
			xml_doc += "<"+key+">"+unicode(value)+"</"+key+">\n"

	xml_doc += "</"+root_element+">\n"

	return xml_doc

def convertJSON2XML(root_element, json_doc):
	""" function to convert a python dict in a xml documento (xml.dom.minidom.Document)
		parameters:  
			root_element, element root for the document
			json_doc, a dictionary (dict) with the json document
		returns:
			xml.dom.minidom.Document
	"""
	xml_document = convertJSON2STR(root_element, json_doc)
	return parseString(xml_document.encode('ascii', 'xmlcharrefreplace').encode("utf-8").replace("\n","").replace("&",""))

def convertList2JSON(list_of_classes):
	""" function to convert a list of classes in a json """
	return json.dumps([convert2JSON(x) for x in list_of_classes])

def convertList2XML(list_of_classes, root_element="list"):
	""" function to convert a list of classes in xml """
	xml_docs = [convert(x,"xml") for x in list_of_classes]
	xml_doc = "<"+root_element+">\n"
	for d in xml_docs:
		xml_doc += d
	xml_doc += "</"+root_element+">"

	return parseString(xml_doc.encode('ascii', 'xmlcharrefreplace').encode("utf-8").replace("\n","").replace("&",""))

def convertMongo2XML(root_element, data):
	""" function to convert a document or documents recovered from mongoDB in a xml document
		parameters:  
			root_element, element root for the document
			data, a dictionary (dict) or a pymongo.cursor.Cursor with the json document
		returns:
			xml.dom.minidom.Document	
	"""
	try:
		import pymongo
	except ImportError:
		raise Exception("You must install pymongo")

	if isinstance(data, pymongo.cursor.Cursor):
		data_list = list(data)
		return convertJSON2XML(root_element,data_list)
	elif isinstance(data,dict):
		return convertJSON2XML(root_element,data)
	else:
		return None

def convertMongo2JSON(data):
	""" function to convert a document or documents recovered from mongoDB in a json document
		parameters:  
			data, a dictionary (dict) or a pymongo.cursor.Cursor with the json document
		returns:
			json (python dictionary)
	"""
	try:
		import pymongo
	except ImportError:
		raise Exception("You must install pymongo")

	if isinstance(data, pymongo.cursor.Cursor):
		l = list()
		for d in list(data):
			l.append(json.loads(json.dumps(d, cls=Encoder)))
		return l
	elif isinstance(data,dict):
		return json.loads(json.dumps(data, cls=Encoder))

def getValue(e):
	""" function that returns the value of a text node from xml element
	"""
	if e[0].childNodes[0].nodeType == e[0].TEXT_NODE:
		return e[0].childNodes[0].nodeValue
	else:
		return e

def convertXML2OBJ(cls, xml):
	""" function to convert xml to python object
		parameters:
			cls, is the class that represents to the xml.
			xml, is the xml element to convert into a python object

			example:
				class Person:
					name = str
					age = int

				<Person>
					<name>Steve</name>
					<age>41</age>
				<Person>
		returns:
			python object
	"""
	cls_dict = {}
	for attr in filter(lambda x : x not in dir(object),dir(cls)):
		attr_type = cls.__dict__[attr]
		xml_value = xml.getElementsByTagName(attr)
		if len(xml_value)>0:
			if isinstance(attr_type,list) and attr_type[0] in [int, float, long, str]:
				cls_dict[attr] = [x.childNodes[0].nodeValue for x in xml_value[0].childNodes if x.nodeType == x.ELEMENT_NODE]
			elif attr_type not in [int, float, long, str] and not hasattr(attr_type,'__module__'):
				l = []
				for xelem in xml.getElementsByTagName(attr_type[0].__name__):
					l.append(convertXML2OBJ(attr_type[0],xelem))
				cls_dict[attr] = l
			elif attr_type not in [int, float, long, str] and hasattr(attr_type,'__module__'):
				cls_dict[attr] = convertXML2OBJ(attr_type,xml_value[0])
			else:
				type_conv = cls.__dict__[attr]
				cls_dict[attr] = type_conv(getValue(xml_value))

	c = cls()
	c.__dict__ = cls_dict
	return c

def convertJSON2OBJ(cls, json_doc):
	""" function that convert an json in a python object
		parameters:
			cls, is the class that represents to the json.
			doc, is the json documment

			example:
				class Person:
					name = str
					age = int

				{
					"name" : "Steve"
					"age"  : 41
				}

		returns:
			python oject
	"""
	attrs = {}
	if isinstance(json_doc,list):
		l = []
		for a in json_doc:
			b = convertJSON2OBJ(cls, a)
			l.append(b)
		return l
	else:
		for key in json_doc.keys():
			value = json_doc[key]
			if not isinstance(value,list) and not isinstance(value,dict):
				type_conv = type(value)
				attrs[key] = type_conv(value)
			elif isinstance(value,dict) and not isinstance(cls.__dict__[key],list):
				attrs[key] = convertJSON2OBJ(cls.__dict__[key],value)
			else:
				l = []
				for a in value:
					b = convertJSON2OBJ(cls.__dict__[key][0], a)
					l.append(b)
				attrs[key] = l
		c = cls()
		c.__dict__ = attrs
		return c
