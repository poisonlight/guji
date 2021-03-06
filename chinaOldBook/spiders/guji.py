# -*- coding: utf-8 -*-
import scrapy
import time
import re
import requests
import urllib.parse
from scrapy import FormRequest
from chinaOldBook.items import ChinaoldbookItem


class GujiSpider(scrapy.Spider):
    name = 'guji'
    start_urls = ['http://guji.artx.cn/']
    login_url = 'http://www.artx.cn/user/login.asp'

    def start_requests(self):
        yield scrapy.Request(self.login_url, callback=self.login)

    def login(self, response):
        formdata = {
            'act': 'submit',
            'duser': '有梦想的麻雀',
            'dpwd': '123456',
            'Submit': '会员登录',
        }
        # string = urllib.parse.urlencode(formdata)
        yield FormRequest.from_response(response, formdata=formdata, callback=self.parse_login)

    def parse_login(self, response):
        # print('>>>>>>>>'+response.text)
        print(response.url)
        if '有梦想的麻雀' in response.text:
            print('登录成功')
            yield from super().start_requests()
            # guji_link = response.xpath("//div[@class='top']/div[@class='top-1']/span/a[2]/@href").extract_first()
            # print(guji_link)
            # yield scrapy.Request(guji_link, callback=self.parse)
        else:
            print('登录失败')

    def parse(self, response):
        buji_classify = response.xpath("//div[@class='dmain']/div[@id='dright']/div[@class='dleft_guji']/div[@class='dg_title'][position()<6]")
        print('来了，老弟儿')
        for bu in buji_classify:
            buji_classify_name = bu.xpath("h1/text()").extract_first()
            buji_classify_list = bu.xpath("h1/following-sibling::a")
            for two_classify in buji_classify_list:
                two_classify_name = two_classify.xpath("text()").extract_first()
                two_classify_link = two_classify.xpath("@href").extract_first()
                yield scrapy.Request(two_classify_link, callback=self.bookClassify, meta={"buji_classify_name": buji_classify_name, "two_classify_name": two_classify_name})

        buji_classify1 = response.xpath("//div[@class='dmain']/div[@id='dright']/div[@class='dleft_guji']/div[@class='dg_title'][position()>6]")

        for wen in buji_classify1:
            buji_classify_name = '古籍文言文'
            buji_classify_list = wen.xpath("p/a[@href='/wyw/']/following-sibling::a")
            for we in buji_classify_list:
                two_classify_name = we.xpath("h2/text()").extract_first()
                two_classify_link = 'http://guji.artx.cn/' + we.xpath("@href").extract_first()
                yield scrapy.Request(two_classify_link, callback=self.wenYanwen, meta={"buji_classify_name": buji_classify_name, "two_classify_name": two_classify_name})

    def wenYanwen(self, response):
        buji_classify_name = response.meta['buji_classify_name']
        two_classify_name = response.meta['two_classify_name']

        guwen_list = response.xpath("//div[@class='dmain']/div[@id='dright']/div[@class='dwyw']/div[@class='dg2']/a")
        for guwen in guwen_list:
            guwen_name = guwen.xpath("text()").extract_first()
            guwen_link = guwen.xpath("@href").extract_first()
            yield scrapy.Request(guwen_link, callback=self.content2, meta={"buji_classify_name": buji_classify_name, "two_classify_name": two_classify_name, "guwen_name": guwen_name})

    def bookClassify(self, response):
        buji_classify_name = response.meta['buji_classify_name']
        two_classify_name = response.meta['two_classify_name']

        book_list = response.xpath("//div[@class='l_mulu_table']/div[@class='l_mulu_list']/ul/li")
        for book in book_list:
            book_name = book.xpath("span/a/text()").extract_first()
            book_link = 'http://guji.artx.cn' + book.xpath("span/a/@href").extract_first()
            yield scrapy.Request(book_link, callback=self.guBook, meta={"buji_classify_name": buji_classify_name, "two_classify_name": two_classify_name, "book_name": book_name})

    def guBook(self, response):
        buji_classify_name = response.meta['buji_classify_name']
        two_classify_name = response.meta['two_classify_name']
        book_name = response.meta['book_name']

        chapter_list = response.xpath("//div[@class='dmain']/div[@id='dright']/div[@class='l_mulu_table']/div[@class='l_mulu_td']/ul/li")
        # headers = {
        #     'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        #     'Accept - Language': 'zh - CN, zh;q = 0.9',
        #     'Cache - Control': 'max - age = 0',
        #     'Connection': 'keep - alive',
        #     'Cookie': 'ftgujiartxcn = 1;bdshare_firstime = 1552900600791;UM_distinctid = 1699016b41e617 - 0bc8d7f06bfa45 - 9333061 - 1fa400 - 1699016b41f5d4;artx % 5Fpwd = a25ac6b331fab22958fcbb2761905dd9;artx % 5Fuserlv = 11;artx % 5Fuserid = 1395475;artx % 5Fusername % 5Futf8 = % E6 % 9C % 89 % E6 % A2 % A6 % E6 % 83 % B3 % E7 % 9A % 84 % E9 % BA % BB % E9 % 9B % 80;artx % 5Fusername = % E6 % 9C % 89 % E6 % A2 % A6 % E6 % 83 % B3 % E7 % 9A % 84 % E9 % BA % BB % E9 % 9B % 80;artx % 5Fchk = cf5bc6016c6a5d6685a98d0a8d59874e;artx % 5Fdaohang =;artx % 5Fshuqian =;ASPSESSIONIDAADSDACR = DNPBHEHBLBDDKPEBOMCANDDL;Hm_lvt_5c695ba8cb9e7c5059b543c35cc1144a = 1552900601, 1552964319, 1553132419;CNZZDATA1254963021 = 2007352500 - 1552895611 - % 7C1553152678;dh % 5Fchecked = checked;guji % 5Fsn % 5Fp = 1;guji % 5Fsn = 16;Hm_lpvt_5c695ba8cb9e7c5059b543c35cc1144a = 1553157111',
        #     'Host': 'guji.artx.cn',
        #     'Referer': book_link,
        #     'Upgrade - Insecure - Requests': '1',
        #     'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.121Safari / 537.36'
        # }
        for chapter in chapter_list:
            time.sleep(1)
            chapter_name = chapter.xpath("a/text()").extract_first()
            chapter_link = 'http://guji.artx.cn' + chapter.xpath("a/@href").extract_first()

            # respon = requests.get(chapter_link, headers)
            # respon.encoding = 'utf-8'
            # print(respon.text)
            #
            # print(chapter_link)
            yield scrapy.Request(chapter_link, callback=self.content, meta={"buji_classify_name": buji_classify_name, "two_classify_name": two_classify_name, "book_name": book_name, "chapter_name": chapter_name})

    def content(self, response):
        buji_classify_name = response.meta['buji_classify_name']
        two_classify_name = response.meta['two_classify_name']
        book_name = response.meta['book_name']
        chapter_name = response.meta['chapter_name']

        content = response.text

        con = re.search('<div id="r_zhengwen">.*<div class="dright_show_foot">', content, re.S).group()
        con1 = con.replace('<div id="r_zhengwen">', '').replace('<div class="dright_show_foot">', '').replace('</div>', '').replace('&nbsp', '').replace('<font class=bj_style>', '').replace('</font>', '').replace('<br>', '</p><p>').replace(r'\u3000', '')
        con2 = re.sub('<a .*?>.*?</a>', '', con1)
        mast_con = con2.replace("</p>", "", 1)
        result = mast_con[::-1]
        result1 = result.replace('>p<', '', 1)
        result2 = result1[::-1]

        item = ChinaoldbookItem()

        item['buji_classify_name'] = buji_classify_name
        item['two_classify_name'] = two_classify_name
        item['book_name'] = book_name
        item['chapter_name'] = chapter_name
        item['content'] = result2

        # print(item)
        yield item

    def content2(self, response):
        buji_classify_name = response.meta['buji_classify_name']
        two_classify_name = response.meta['two_classify_name']
        guwen_name = response.meta['guwen_name']

        content = response.text

        con = re.search('<div id="r_zhengwen">.*<div class="dleft">', content, re.S).group()
        con1 = con.replace('<div id="r_zhengwen">', '').replace('<div class="dright_show_foot">', '').replace('</div>', '').replace('&nbsp', '').replace('<font class=bj_style>', '').replace('</font>', '').replace('<br>', '</p><p>').replace(r'\u3000', '').replace(r'<div class="dleft">', '')
        con2 = re.sub('<a .*?>.*?</a>', '', con1)
        mast_con = con2.replace("</p>", "", 1)
        result = mast_con[::-1]
        result1 = result.replace('>p<', '', 1)
        mastcontent = result1[::-1]

        item = ChinaoldbookItem()

        item['buji_classify_name'] = buji_classify_name
        item['two_classify_name'] = two_classify_name
        item['book_name'] = guwen_name
        item['chapter_name'] = ''
        item['content'] = mastcontent
        # print(item)
        yield item
