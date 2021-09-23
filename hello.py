#!/usr/bin/env python3
import os

print("Content-Type: text/html") 
print()  
print("<title>test</title>")
print("<p>Hello World!</p>")

print(os.environ.keys())

for param in os.environ.keys():
    if (param=='QUERY_STRING'):
        print ("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

for param in os.environ.keys():
    if (param=='HTTP_USER_AGENT'):
        print ("<b>%20s</b>: %s<br>" % (param, os.environ[param]))