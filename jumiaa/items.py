# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JumiaaItem(scrapy.Item):
    Name = scrapy.Field()
    Price = scrapy.Field()
    Image = scrapy.Field()
    Deal = scrapy.Field()
