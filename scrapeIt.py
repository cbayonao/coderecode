import scrapy


class ScrapeitSpider(scrapy.Spider):
    name = 'scrapeIt'
    start_urls = ['http://scrapeit.home.blog/']

    def parse(self, response):
        articles = response.css('article')
        for article in articles:
            posts = {
                'title': article.css('h2.entry-title a::text').get(),
                'paragraph': article.css('div.entry-content p::text').get(),
                'author': article.css('span.author.vcard a::text').get(),
                'created_at': article.css('time.entry-date.published::text').get(),
                'categories': article.css('span.cat-links a::text').getall()
            }
            yield posts
