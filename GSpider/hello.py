import sys
import os
import time
import json

spider_properties = {}

spider_properties["name"] = "google"
spider_properties["allowed_domains"] = ["google.com"]
spider_properties["start_urls"] = ['http://www.google.com']
print (json.dumps(spider_properties))


for line in sys.stdin:
    print "FROM CLIENT" + line

#print "ADD 1 2"

#for line in sys.stdin:
#	print "RESULT IS " + line 
