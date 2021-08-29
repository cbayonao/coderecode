import scrapy


class TocwikiSpider(scrapy.Spider):
    name = 'tocWiki'
    allowed_domains = ['en.wikipedia.org/wiki/Python_(programming_language)']
    start_urls = [
        'http://en.wikipedia.org/wiki/Python_(programming_language)']

    def parse(self, response):
        self.log(f'Got response from {response.url}')
        list_key = response.css('.tocnumber::text').getall()
        list_values = response.css('span.toctext::text').getall()
        content = {}
        for value, key in zip(list_values, list_key):
            content[key] = value
        yield content
