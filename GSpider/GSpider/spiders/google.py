from scrapy.spider import Spider
from twisted.internet import protocol
from twisted.internet import reactor
import json
import time

DATA = ""

class MyPP(protocol.ProcessProtocol):
    def __init__(self, verses):
        self.verses = verses
        self.data = ""
    def connectionMade(self):
        print "connectionMade!"
        #self.transport.write("I AM FAISAL !!!")
        #self.transport.closeStdin()

    def send_DATA(self, data="HELLLLLOO"):
        print "Sending Data"
        self.transport.write(data)
        self.transport.closeStdin()
        
    def outReceived(self, data):
        print "outReceived! with %d bytes!" % len(data)
        DATA = self.data
        self.data = self.data + data
        print "Received data: "+ str(data)
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

pp=MyPP(10)

class GoogleSpider(Spider):
    
    name = "google"
    allowed_domains = ["google.com"]
    start_urls = [
        'http://www.google.com',
        ]
    
    '''
    name = "google"
    allowed_domains = []
    start_urls = []
    '''
    def __init__(self, Input=None, *args, **kwargs):
        super(GoogleSpider, self).__init__(*args, **kwargs)
        
        #Find out how to run reactor.spawn process before the spider initialization
        reactor.spawnProcess(pp, "python", ["python", str(Input)], {})
    	print "THIIS IS IT" + str(DATA)
    	'''
    	spider_props = json.loads(pp.data)
    	self.name = str(spider_props["name"])
    	self.allowed_domains = ((spider_props["allowed_domains"]))
    	self.start_urls = ((spider_props["start_urls"]))
        '''
        #reactor.callWhenRunning(pp.send_DATA)
        #reactor.run()
        

    def parse(self, response):
    	pp.transport.write(str(response.body))
    	pp.transport.closeStdin()
    	#pp.transport.write("I AM FAISAL2 !!!")
    	#pp.transport.closeStdin()
    	
    	#print response.request.url
        pass 
