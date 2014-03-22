#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from twisted.internet import protocol
from twisted.internet import reactor
import re
from time import sleep
import sys

class MyPP(protocol.ProcessProtocol):
    def __init__(self, verses):
        self.verses = verses
        self.data = ""

    def send_DATA(self, data="HELLLLLOO"):
        print "Sending Data"
        self.transport.write(data)
        self.transport.closeStdin()

    def connectionMade(self):
        print "connectionMade!"
        #pass
    def outReceived(self, data):
        print "outReceived! with %d bytes!" % len(data)
        print "RECEIVED:"+data
    

    def errReceived(self, data):
        print "errReceived! with %d bytes!" % len(data)
    def inConnectionLost(self):
        print "inConnectionLost! stdin is closed! (we probably did it)"
    def outConnectionLost(self):
        print "outConnectionLost! The child closed their stdout!"
        # now is the time to examine what they wrote
        #print "I saw them write:", self.data
        #(dummy, lines, words, chars, file) = re.split(r'\s+', self.data)
        #print "I saw %s lines" % lines

    def errConnectionLost(self):
        print "errConnectionLost! The child closed their stderr."
    def processExited(self, reason):
        print "processExited, status %d" % (reason.value.exitCode,)
    def processEnded(self, reason):
        print "processEnded, status %d" % (reason.value.exitCode,)
        print "quitting"
        reactor.stop()

for i in range(0,10):
    print i
pp = MyPP(10)
#reactor.run()
def sendMsg():
    print "ENTERED"
    msg1="Sending first message\n"
    len1=str(len(msg1))
    len1 = len1 + "\n"
    pp.transport.write(len1)
    #pp.transport.closeStdin()
    #sys.stdin.write(len1)
    pp.transport.write(msg1)
    #pp.transport.closeStdin()
    #sys.stdin.write(msg1)
    
    msg2="Sending second message\n"
    len2=str(len(msg2))
    len2 = len2 + "\n"
    pp.transport.write(len2)
    pp.transport.closeStdin()
    pp.transport.write(msg2)
    pp.transport.closeStdin()
    
# use -u option because python buffers output by default when writing to a pipe (when invoked from spawnProcess), thus 
# it wont actually write anything until it has accumulated around 4096 bytes 
reactor.spawnProcess(pp, "python", ["python","-u" ,"hello.py"], {})
reactor.callWhenRunning(sendMsg)
reactor.run()



#pp.transport.write("HELLO WORLD")
#pp.transport.closeStdin()

