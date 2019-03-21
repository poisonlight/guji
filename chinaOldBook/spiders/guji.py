# -*- coding: utf-8 -*-
import scrapy


class GujiSpider(scrapy.Spider):
    name = 'guji'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
