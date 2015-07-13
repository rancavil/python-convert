from pyconvert.pyconv import convertXML2OBJ, convert2XML, convert2JSON
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
     isbn = long
     language = str
     title = str
     authors = [str]
     url = str

xml = parseString(xmlDoc)
obj = convertXML2OBJ(Book,xml.documentElement)

print "isbn     : %ld "%obj.isbn
print "language : %s  "%obj.language
print "title    : %s  "%obj.title
print "url      : %s  "%obj.url
print "Authors"
for author in obj.authors:
     print "\t %s "%author

print
print obj.__dict__
print obj.__class__.__name__
print
rc = convert2JSON(obj)
print rc
