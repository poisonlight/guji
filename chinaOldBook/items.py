# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaoldbookItem(scrapy.Item):
    # define the fields for your item here like:
    buji_classify_name = scrapy.Field()
    two_classify_name = scrapy.Field()
    book_name = scrapy.Field()
    chapter_name = scrapy.Field()
    content = scrapy.Field()
