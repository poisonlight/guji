# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import time


class ChinaoldbookPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def process_item(self, item, spider):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='hwss', charset='utf8')
        self.cursor = self.db.cursor()

        buji_classify_na = item['buji_classify_name']

        try:
            select_table1 = "SELECT buji_classify_name FROM hw_chinaguji_bujiclassify"
            self.cursor.execute(select_table1)
            result = self.cursor.fetchall()

            buji_classify_list = []
            for i in result:
                a = str(i).strip().replace("'", "").replace("(", "").replace(")", "").replace(",", "")
                buji_classify_list.append(a)

            buji_classify_name = buji_classify_na.strip().replace("(", "").replace(")", "")

            if buji_classify_name not in buji_classify_list:
                insert_table1 = "INSERT INTO hw_chinaguji_bujiclassify(buji_classify_name) VALUES ('%s')"%(buji_classify_na)
                self.cursor.execute(insert_table1)
                print('{} 部级分类名称插入成功'.format(buji_classify_na))
        except:
            print('{} 部级分类名称插入失败'.format(buji_classify_na))


        book_classify_na = item['two_classify_name']

        try:
            # 查询部级下面的分类是否存在书籍分类表里面
            select_table2 = "SELECT bookclassify_name FROM hw_chinaguji_bookclassify"
            self.cursor.execute(select_table2)
            result = self.cursor.fetchall()

            book_classify_list = []
            for i in result:
                a = str(i).strip().replace("'", "").replace("(", "").replace(")", "").replace(",", "")
                book_classify_list.append(a)

            select_minister_id = "SELECT buji_id FROM hw_chinaguji_bujiclassify WHERE buji_classify_name='%s'" % (buji_classify_name)
            self.cursor.execute(select_minister_id)
            reault = self.cursor.fetchone()
            buji_id = int(str(reault).strip().replace(",", "").replace("(", "").replace(")", ""))

            book_classify_name = book_classify_na.strip().replace("(", "").replace(")", "")

            if book_classify_name not in book_classify_list:
                sql_insert_bookclassify = "INSERT INTO hw_chinaguji_bookclassify(bookclassify_name, relation_bujiclassify_id) VALUES('%s', '%d')" %(book_classify_na, buji_id)
                self.cursor.execute(sql_insert_bookclassify)
                print('{} 分类名称插入成功'.format(book_classify_na))
        except:
            print('{} 分类名称插入失败'.format(book_classify_na))


        book_na = item['book_name']

        try:
            # 查询书籍名称是否存在书籍名称表里面
            select_table3 = "SELECT bookname FROM hw_chinaguji_bookname"
            self.cursor.execute(select_table3)
            result = self.cursor.fetchall()

            bookname_list = []
            for i in result:
                a = str(i).strip().replace("'", "").replace("(", "").replace(")", "").replace(",", "")
                bookname_list.append(a)
            # print(bookname_list)
            # print(book_name)
            select_bookclassify_id = "SELECT bookclassify_id FROM hw_chinaguji_bookclassify WHERE bookclassify_name='%s'" % (book_classify_name)
            self.cursor.execute(select_bookclassify_id)
            reault = self.cursor.fetchone()
            buji_id = int(str(reault).strip().replace(",", "").replace("(", "").replace(")", ""))

            book_name = book_na.strip().replace("(", "").replace(")", "")  # 同样去掉括号，防止字符串中有括号导致数据插入重复

            if book_name not in bookname_list:
                sql_insert_bookname = "INSERT INTO hw_chinaguji_bookname(bookname, relation_classify_id) VALUES('%s', '%d')" % (book_na, buji_id)
                self.cursor.execute(sql_insert_bookname)
                print('{} 书籍名称插入成功'.format(book_na))
        except:
            # pass
            print('{} 书籍名称插入失败'.format(book_na))


        chapter_na = item['chapter_name']
        content = item['content']

        try:
            # 查询章节名称是否存在章节内容表里面
            select_bookname_id = "SELECT bookname_id FROM hw_chinaguji_bookname WHERE bookname='%s'" % (book_na)
            self.cursor.execute(select_bookname_id)
            reault = self.cursor.fetchone()
            buji_id = int(str(reault).strip().replace(",", "").replace("(", "").replace(")", ""))

            select_table4 = "SELECT chapter_name,relation_bookname_id FROM hw_chinaguji_content"
            self.cursor.execute(select_table4)
            result = self.cursor.fetchall()

            bookchapter_list = []
            global abc
            for i in result:
                abc = str(i).strip().replace("'", "").replace("(", "").replace(")", "").replace(",", "")
                bookchapter_list.append(abc)

            chapter_name = chapter_na.strip().replace("(", "").replace(")", "")

            newstr = chapter_name + ' ' + str(buji_id)

            if newstr not in bookchapter_list:
                time.sleep(1)
                sql_insert_chaptercontent = "INSERT INTO hw_chinaguji_content(chapter_name, chapter_content, relation_bookname_id) VALUES('%s', '%s', '%d')" % (chapter_name, content, buji_id)
                self.cursor.execute(sql_insert_chaptercontent)
                print('{} 章节内容插入成功'.format(book_na))
        except:
            print('{} 章节内容插入失败'.format(book_na))

        self.db.commit()
        self.cursor.close()
        self.db.close()

