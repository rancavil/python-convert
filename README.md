PyConvert
=========

Converts python objects in xml or json documents

Installation
------------

You must have installed python 2.7.

Download the api from github (https://github.com/rancavil/python-convert/archive/master.zip).

Unzip python-convert-master.zip

     $ unzip python-convert-master.zip

Go to the directory and install the api.

     $ cd python-convert-master
     $ python setup.py install

Or you can install it using.

     $ pip install pyconvert

Example
-------

With pyconvert you can transform and serialize a python object in a xml or json document.

Examples:

Convert a python object in a python dictionary (json).
------------------------------------------------------
Create the file example_json.py

     #!/usr/bin/env python

     import pyconvert.pyconv

     class Person(object):
          def __init__(self, name, age):
          	self.name = name
          	self.age = age

     p = Person("Rodrigo",30)

     json_person = pyconvert.pyconv.convert2JSON(p)
     print json_person
     print "name : %s"%json_person['name']
     print "age  : %d"%json_person['age']

This example convert a python object Person in a python dict (json document).

     $ python example_json.py

The output must be:

     {u'age':30, u'name':u'Rodrigo'}
     name : Rodrigo
     age  : 30

Convert a python object in a python xml.dom.minidom.Document (xml).
-------------------------------------------------------------------
Create the file example_xml.py

     #!/usr/bin/env python

     import pyconvert.pyconv

     class Person(object):
          def __init__(self, name, age):
          	self.name = name
          	self.age = age

     p = Person("Rodrigo",30)

     xml_person = pyconvert.pyconv.convert2XML(p)
     print xml_person.toprettyxml()

This example convert a python object Person in a python xml.dom.minidom.Document.

     $ python example_xml.py

The output must be:

     <?xml version="1.0" ?>
     <Person>
          <age>30</age>
          <name>Rodrigo</name>
     </Person>

A little more complex example.
------------------------------
Create a file called example_order.py

     #!/usr/bin/env python
     
     import pyconvert.pyconv
     
     class Book(object):
          isbn = int
          name = str

     class Order(object):
          number = int
          book = [Book]
     
     b1 = Book()
     b1.isbn = 135573023167
     b1.name = "Learning Python"
     
     b2 = Book()
     b2.isbn = 978602122321
     b2.name = "Temporada de Zopilotes"

     order = Order()
     order.number = 331
     order.book = [b1,b2]

     print
     json_doc = pyconvert.pyconv.convert2JSON(order)
     print json_doc
     print
     xml_doc = pyconvert.pyconv.convert2XML(order)
     print xml_doc.toprettyxml()

Save and execute the example:

     $ python example_order.py

The output must be:

     {u'books': [
     		{u'isbn': 135573023167, u'name': u'Learning Python'}, 
     		{u'isbn': 978602122321, u'name': u'Temporada de Zopilotes'}
     		], 
     u'number': 331}

     <?xml version="1.0" ?>
     <Order>
	    <books>
		  <Book>
			<isbn>135573023167</isbn>
			<name>Learning Python</name>
		  </Book>
		  <Book>
			<isbn>978602122321</isbn>
			<name>Temporada de Zopilotes</name>
		  </Book>
	    </books>
        <number>331</number>
     </Order>

Create a file called example_music.py

     #!/usr/bin/env python
     
     import pyconvert.pyconv
     
     class Band(object):
        name_band = str
        year_band = int

     class Album(object):
        band_album = Band
        name_album = str
        year_album = int
        song = [str]

     band = Band()
     band.name_band = "Led Zeppelin"
     band.year_band = 1968
     
     album = Album()
     album.band_album = band
     album.name_album = "House of Holy"
     album.year_album = 1973
     album.song = list()
     album.song.append("The Song Remains the Same")
     album.song.append("The Rain Song")
     album.song.append("Over the Hills and Far Away")
     album.song.append("The Crunge")
     album.song.append("Dancing Days")
     album.song.append("D'yer Mak'er")
     album.song.append("No Quarter")
     album.song.append("The Ocean")

     print
     json_doc = pyconvert.pyconv.convert2JSON(album)
     print json_doc
     print
     xml_doc = pyconvert.pyconv.convert2XML(album)
     print xml_doc.toprettyxml()

Save and execute the program:

     $ python example_music.py

You must see the next output.

     {u'year_album': 1973, 
      u'name_album': u'House of Holy', 
      u'songs': [
           u'The Song Remains the Same', 
           u'The Rain Song', 
           u'Over the Hills and Far Away', 
           u'The Crunge', 
           u'Dancing Days', 
           u"D'yer Mak'er", 
           u'No Quarter', 
           u'The Ocean'], 
     u'band_album': {u'name_band': u'Led Zeppelin', 
                     u'year_band': 1968}
     }

     <?xml version="1.0" ?>
     <Album>
          <year_album>1973</year_album>
             <songs>
                <song>The Song Remains the Same</song>
                <song>The Rain Song</song>
                <song>Over the Hills and Far Away</song>
                <song>The Crunge</song>
                <song>Dancing Days</song>
                <song>D'yer Mak'er</song>
                <song>No Quarter</song>
                <song>The Ocean</song>
             </songs>
          <name_album>House of Holy</name_album>
          <Band>
                <name_band>Led Zeppelin</name_band>
                <year_band>1968</year_band>
          </Band>
      </Album>
