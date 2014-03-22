import sys


len1 = sys.stdin.readline()
len1 = len1.split('\n')[0]
len1 = int(len1)
print "Len of first msg is "+ str(len1) + "\n"
msg1 = sys.stdin.read(len1)
print "FROM CLIENT: "+msg1


len2 = sys.stdin.readline()
len2 = len2.split('\n')[0]
len2 = int(len2)
print "Len of second msg is "+ str(len2) + "\n"
msg2 = sys.stdin.read(len2)
print "FROM CLIENT: "+msg2



#for line in sys.stdin:
#	print "RESULT IS " + line 
