from scrapy.spider import Spider

class ExampleSpider(Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = (
        'http://www.example.com/',
        )

    def parse(self, response):
        pass 
