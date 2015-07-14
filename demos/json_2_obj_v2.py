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
print "JSON original"
print "*************"
print json.dumps(doc, sort_keys=True, indent=2, separators=(',',': '))
print
print "Python obj     "
print "***************"
print "Message        "
print "---------------"
print "num  : %d "%c.num
print "text : %s "%c.text
print
print "Sender         "
print "---------------"
print "c.sender.userid   : %d "%c.sender.userid
print "c.sender.username : %s "%c.sender.username
print "Receiver       "
print "---------------"
print "c.receiver.userid   : %d "%c.receiver.userid
print "c.receiver.username : %s "%c.receiver.username
print
