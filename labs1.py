#!/usr/bin/python
#Aaron Avila
#Lab 6: The Scripting Lab

i=0

while(i<10):
	file = "file%d" % i
	f = open(file, "w+")
	f.write("Hello, this is the first line of %s" % file +"\n")
	f.close()
	i += 1
