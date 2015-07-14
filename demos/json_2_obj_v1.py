from pyconvert.pyconv import convertJSON2OBJ
import json

doc = {'userid':10010, 'username':'homerJ', 'projects' : [ {"seq" : 1, "name" : "API Develop"}, {"seq": 2, "name" : "Java Apps"}]}

class Project(object):
	seq = int
	name = str

class User(object):
	userid = int
	username = str
	projects = [Project]

c = convertJSON2OBJ(User,doc)
print "JSON original"
print "*************"
print json.dumps(doc, sort_keys=True, indent=2, separators=(',',': '))
print
print "Python obj     "
print "***************"
print "User data      "
print "---------------"
print "userid   : %d "%c.userid
print "username : %s "%c.username
print
print "User's projects"
print "---------------"
for project in c.projects:
	print "\tprojects.seq  : %d "%project.seq 
	print "\tprojects.name : %s "%project.name
	print
