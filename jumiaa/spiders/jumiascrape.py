import scrapy
from ..items import JumiaaItem


class JumiascrapeSpider(scrapy.Spider):
    name = "jumiascrape"
    allowed_domains = ["www.jumia.com.ng"]
    # start_urls = ["https://www.jumia.com.ng"]
    start_urls = ["https://www.jumia.com.ng/catalog/?q=watches"]
    # https://www.jumia.com.ng/catalog/?q=watches&page=50#catalog-listing


    def parse(self, response):
        products = response.css('article.prd._fb.col.c-prd')
        for product in products:
            name = product.css('h3.name::text').get()
            price = product.css('div.prc::text').get()
            image = product.css('div.img-c img').attrib['data-src']
            deal = product.css('div.img-c span::text').get()

            jumiastore = JumiaaItem()
            jumiastore['Name'] = name
            jumiastore['Price'] = price
            jumiastore['Image'] = image
            jumiastore['Deal'] = deal

            yield jumiastore
        
        for x in range(2, 6):
            next_page = f'https://www.jumia.com.ng/catalog/?q=watches&page={x}#catalog-listing'
            yield response.follow(next_page, callback=self.parse)