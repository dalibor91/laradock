#!/usr/bin/python

import sys
import os

data = {
   'template' : None,
   'volumes' : None, 
   'ports' : None, 
   'location': None
}

def read_file(f):
	data = ""
	with open(f) as u:
		for i in u.readlines():
			yield i.strip()

_next=None
for i in sys.argv[1:]:
	if _next is not None:
		data[_next] = i
		_next = None
		continue

	if i == '-tpl':
		_next = 'template'
		continue
	elif i == '-v':
		_next = 'volumes'
		continue
	elif i == '-p':
		_next = 'ports'
		continue
	elif i == '-l':
		_next = 'location'

for k,v in data.items():
	if v is None:
		print("%s is not set" % k)
		sys.exit(1)





with open(data['template']) as tpl:
	newTpl = "" 
	for i in tpl.readlines():
		if i.strip() == '{volumes}':
			ident = (i.split("{",1)[0].count(" "))*" "
			for j in read_file(data['volumes']):
				newTpl += "%s- %s\n" % (ident, j)
		elif i.strip() == '{ports}':
			ident = (i.split("{",1)[0].count(" "))*" "
			for j in read_file(data['ports']):
				newTpl += "%s- %s\n" % (ident, j)
		else: 
			newTpl += "%s"%i
	newTpl = newTpl.replace('{location}', os.path.realpath(data['location']))
	print newTpl

sys.exit(0)





