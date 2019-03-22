# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class ChinaoldbookPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def process_item(self, item, spider):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='hwss', charset='utf8')
        self.cursor = self.db.cursor()

        delete_table = "DROP TABLE hw_chinaguji_bujiclassify"
        try:
            self.cursor.execute(delete_table)
            print('删除部级分类表成功')
        except:
            print('删除部级分类表失败')

        create_table1_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_bujiclassify (
                            id INT NOT NULL AUTO_INCREMENT,
                            buji_classify_name varchar(80) NOT NULL,
                            PRIMARY KEY (id))
                            ENGINE=InnoDB, DEFAULT CHARSET=utf8
                            """
        try:
            self.cursor.execute(create_table1_sql)
            print('部级分类表创建成功')
        except:
            print('部级分类表创建失败')





