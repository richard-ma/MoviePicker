# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieFirstItem(scrapy.Item):
    name = scrapy.Field()
    site = scrapy.Field()


class MoviepickerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
