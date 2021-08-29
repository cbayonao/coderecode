import scrapy


class BlogpaginationSpider(scrapy.Spider):
    name = 'blogPagination'
    start_urls = ['http://scrapeit.home.blog/']

    def parse(self, response):
        self.log(f'Got response from {response.url}')
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
        next_page_url = response.css('a.next.page-numbers::attr(href)').get()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            # Create a new request object
            yield scrapy.Request(url=next_page_url, callback=self.parse)
