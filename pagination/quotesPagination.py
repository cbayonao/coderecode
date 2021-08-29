import scrapy


class QuotespaginationSpider(scrapy.Spider):
    name = 'quotesPagination'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        """Callback method
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
        next_page_url = response.css('li.next a::attr(href)').get()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            # Create a new request object
            yield scrapy.Request(url=next_page_url, callback=self.parse)
