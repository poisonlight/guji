# -*- coding: utf-8 -*-
import scrapy
import time


class GujiSpider(scrapy.Spider):
    name = 'guji'
    start_urls = ['http://guji.artx.cn/']

    def parse(self, response):
        buji_classify = response.xpath("//div[@class='dmain']/div[@id='dright']/div[@class='dleft_guji']/div[@class='dg_title'][position()<6]")
        for bu in buji_classify:
            buji_classify_name = bu.xpath("h1/text()").extract_first()
            buji_classify_list = bu.xpath("h1/following-sibling::a")
            for two_classify in buji_classify_list:
                two_classify_name = two_classify.xpath("text()").extract_first()
                two_classify_link = two_classify.xpath("@href").extract_first()
                yield scrapy.Request(two_classify_link, callback=self.bookClassify, meta={"buji_classify_name": buji_classify_name, "two_classify_name": two_classify_name})

    def bookClassify(self, response):
        buji_classify_name = response.meta['buji_classify_name']
        two_classify_name = response.meta['two_classify_name']

        book_list = response.xpath("//div[@class='l_mulu_table']/div[@class='l_mulu_list']/ul/li")
        for book in book_list:
            book_name = book.xpath("span/a/text()").extract_first()
            book_link = 'http://guji.artx.cn' + book.xpath("span/a/@href").extract_first()
            yield scrapy.Request(book_link, callback=self.guBook, meta={"buji_classify_name": buji_classify_name, "two_classify_name": two_classify_name, "book_name": book_name, "book_link": book_link})

    def guBook(self, response):
        buji_classify_name = response.meta['buji_classify_name']
        two_classify_name = response.meta['two_classify_name']
        book_name = response.meta['book_name']


        chapter_list = response.xpath("//div[@class='dmain']/div[@id='dright']/div[@class='l_mulu_table']/div[@class='l_mulu_td']/ul/li")
        for chapter in chapter_list:
            time.sleep(1)
            chapter_name = chapter.xpath("a/text()").extract_first()
            chapter_link = 'http://guji.artx.cn' + chapter.xpath("a/@href").extract_first()
            yield scrapy.Request(chapter_link, callback=self.content, meta={"buji_classify_name": buji_classify_name, "two_classify_name": two_classify_name, "book_name": book_name, "chapter_name": chapter_name})

    def content(self, response):
        buji_classify_name = response.meta['buji_classify_name']
        two_classify_name = response.meta['two_classify_name']
        book_name = response.meta['book_name']
        chapter_name = response.meta['chapter_name']

        print(response.text)
        # print(response.headers)

