import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        """Parsing data from url destination
        :param response:
        :param response:
        :return:
        """
        self.log(f'Got response from {response.url}')
        quotes = response.css('.quote')
        for quote in quotes:
            item = {
                'author': quote.css('.author::text').get(),
                'quote': quote.css('.text::text').get(),
                'tags': quote.css('.tag::text').getall()
            }
            yield item
