import requests
import pymysql

# url = 'http://guji.artx.cn/article/19067.html'
# url = 'http://guji.artx.cn/article/3192.html'
#
# headers = {
#         'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
#         'Accept - Language': 'zh - CN, zh;q = 0.9',
#         'Cache - Control': 'max - age = 0',
#         'Connection': 'keep - alive',
#         'Cookie': 'ftgujiartxcn = 1;bdshare_firstime = 1552900600791;UM_distinctid = 1699016b41e617 - 0bc8d7f06bfa45 - 9333061 - 1fa400 - 1699016b41f5d4;artx % 5Fpwd = a25ac6b331fab22958fcbb2761905dd9;artx % 5Fuserlv = 11;artx % 5Fuserid = 1395475;artx % 5Fusername % 5Futf8 = % E6 % 9C % 89 % E6 % A2 % A6 % E6 % 83 % B3 % E7 % 9A % 84 % E9 % BA % BB % E9 % 9B % 80;artx % 5Fusername = % E6 % 9C % 89 % E6 % A2 % A6 % E6 % 83 % B3 % E7 % 9A % 84 % E9 % BA % BB % E9 % 9B % 80;artx % 5Fchk = cf5bc6016c6a5d6685a98d0a8d59874e;artx % 5Fdaohang =;artx % 5Fshuqian =;ASPSESSIONIDAADSDACR = DNPBHEHBLBDDKPEBOMCANDDL;Hm_lvt_5c695ba8cb9e7c5059b543c35cc1144a = 1552900601, 1552964319, 1553132419;CNZZDATA1254963021 = 2007352500 - 1552895611 - % 7C1553152678;dh % 5Fchecked = checked;guji % 5Fsn % 5Fp = 1;guji % 5Fsn = 16;Hm_lpvt_5c695ba8cb9e7c5059b543c35cc1144a = 1553157111',
#         'Host': 'guji.artx.cn',
#         # 'Referer': book_link,
#         'Upgrade - Insecure - Requests': '1',
#         'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.121Safari / 537.36'
# }
#
# response = requests.get(url, headers)
# print(response.text)



db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='hwss', charset='utf8')
cursor = db.cursor()

delete_table4 = "DROP TABLE hw_chinaguji_content"
delete_table3 = "DROP TABLE hw_chinaguji_bookname"
delete_table2 = "DROP TABLE hw_chinaguji_bookclassify"
delete_table1 = "DROP TABLE hw_chinaguji_bujiclassify"
try:
    cursor.execute(delete_table4)
    print('删除章节内容表成功')
    cursor.execute(delete_table3)
    print('删除书籍名称表成功')
    cursor.execute(delete_table2)
    print('删除书籍分类表成功')
    cursor.execute(delete_table1)
    print('删除部级分类表成功')
except:
    print('删除表失败')

# create_table1_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_bujiclassify (
#                     buji_id INT(11) NOT NULL AUTO_INCREMENT COMMENT '部级编号ID',
#                     buji_classify_name varchar(80) NOT NULL COMMENT '部级名称',
#                     PRIMARY KEY (buji_id),
#                     INDEX(buji_id))
#                     ENGINE=InnoDB, CHARACTER SET utf8 COLLATE utf8_general_ci;"""
#
# try:
#     cursor.execute(create_table1_sql)
#     print('部级分类表创建成功')
# except:
#     print('部级分类表创建失败')
#
#
# create_table2_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_bookclassify (
#                     bookclassify_id INT(11) NOT NULL AUTO_INCREMENT COMMENT '书籍分类编号ID',
#                     bookclassify_name VARCHAR (100) NOT NULL COMMENT '书籍分类名称',
#                     relation_bujiclassify_id INT(11) NOT NULL COMMENT '关联部级分类编号ID',
#                     PRIMARY KEY (bookclassify_id),
#                     FOREIGN KEY(relation_bujiclassify_id) REFERENCES hw_chinaguji_bujiclassify(buji_id) on delete cascade on update cascade)
#                     ENGINE=InnoDB CHARACTER SET utf8 COLLATE utf8_general_ci;"""
#
# try:
#     cursor.execute(create_table2_sql)
#     print('书籍分类表创建成功')
# except:
#     print('书籍分类表创建失败')
#
#
# create_table3_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_bookname (
#                     bookname_id INT(11) NOT NULL AUTO_INCREMENT COMMENT '书籍编号ID',
#                     bookname VARCHAR (200) NOT NULL COMMENT '书籍名称',
#                     relation_classify_id INT(11) NOT NULL COMMENT '关联书籍分类编号ID',
#                     PRIMARY KEY (bookname_id),
#                     FOREIGN KEY(relation_classify_id) REFERENCES hw_chinaguji_bookclassify(bookclassify_id) on delete cascade on update cascade)
#                     ENGINE=InnoDB CHARACTER SET utf8 COLLATE utf8_general_ci;"""
#
# try:
#     cursor.execute(create_table3_sql)
#     print('书籍名称表创建成功')
# except:
#     print('书籍名称表创建失败')
#
#
# create_table4_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_content (
#                     content_id INT(11) NOT NULL AUTO_INCREMENT COMMENT '章节内容编号ID',
#                     chapter_name VARCHAR (300) NOT NULL COMMENT '章节名称',
#                     chapter_content LONGTEXT NOT NULL COMMENT '章节内容',
#                     relation_bookname_id INT(11) NOT NULL COMMENT '关联书籍编号ID',
#                     PRIMARY KEY (content_id),
#                     FOREIGN KEY(relation_bookname_id) REFERENCES hw_chinaguji_bookname(bookname_id) on delete cascade on update cascade)
#                     ENGINE=InnoDB CHARACTER SET utf8 COLLATE utf8_general_ci;"""
#
# try:
#     cursor.execute(create_table4_sql)
#     print('章节内容表创建成功')
# except:
#     print('章节内容表创建失败')
#
#
# buji_classify_name = 'nihao'
#
# try:
#     select_table1 = "SELECT buji_classify_name FROM hw_chinaguji_bujiclassify"
#     cursor.execute(select_table1)
#     result = cursor.fetchall()
#
#     buji_classify_list = []
#     for i in result:
#         a = str(i).strip().replace("'", "").replace("(", "").replace(")", "").replace(",", "")
#         buji_classify_list.append(a)
#
#     if buji_classify_name not in buji_classify_list:
#         insert_table1 = "INSERT INTO hw_chinaguji_bujiclassify(buji_classify_name) VALUES ('%s')"%(buji_classify_name)
#         cursor.execute(insert_table1)
#         print('{} 部级分类名称插入成功'.format(buji_classify_name))
# except:
#     print('{} 部级分类名称插入失败'.format(buji_classify_name))
#
#
# book_classify_name = 'nihao'
#
# try:
#     # 查询部级下面的分类是否存在书籍分类表里面
#     select_table2 = "SELECT bookclassify_name FROM hw_chinaguji_bookclassify"
#     cursor.execute(select_table2)
#     result = cursor.fetchall()
#
#     book_classify_list = []
#     for i in result:
#         a = str(i).strip().replace("'", "").replace("(", "").replace(")", "").replace(",", "")
#         book_classify_list.append(a)
#
#     select_minister_id = "SELECT buji_id FROM hw_chinaguji_bujiclassify WHERE buji_classify_name='%s'" % (buji_classify_name)
#     cursor.execute(select_minister_id)
#     reault = cursor.fetchone()
#     buji_id = int(str(reault).strip().replace(",", "").replace("(", "").replace(")", ""))
#     # print(buji_id)
#
#     if book_classify_name not in book_classify_list:
#         sql_insert_bookclassify = "INSERT INTO hw_chinaguji_bookclassify(bookclassify_name, relation_bujiclassify_id) VALUES('%s', '%d')" %(book_classify_name, buji_id)
#         cursor.execute(sql_insert_bookclassify)
#         print('{} 分类名称插入成功'.format(book_classify_name))
# except:
#     print('{} 分类名称插入失败'.format(book_classify_name))
#
#
# book_name = 'nihao'
#
# try:
#     # 查询书籍名称是否存在书籍名称表里面
#     select_table3 = "SELECT bookname FROM hw_chinaguji_bookname"
#     cursor.execute(select_table3)
#     result = cursor.fetchall()
#
#     bookname_list = []
#     for i in result:
#         a = str(i).strip().replace("'", "").replace("(", "").replace(")", "").replace(",", "")
#         bookname_list.append(a)
#
#     select_bookclassify_id = "SELECT bookclassify_id FROM hw_chinaguji_bookclassify WHERE bookclassify_name='%s'" % (book_classify_name)
#     cursor.execute(select_bookclassify_id)
#     reault = cursor.fetchone()
#     buji_id = int(str(reault).strip().replace(",", "").replace("(", "").replace(")", ""))
#
#     if book_name not in bookname_list:
#         sql_insert_bookname = "INSERT INTO hw_chinaguji_bookname(bookname, relation_classify_id) VALUES('%s', '%d')" % (book_name, buji_id)
#         cursor.execute(sql_insert_bookname)
#         print('{} 书籍名称插入成功'.format(book_name))
# except:
#     print('{} 书籍名称插入失败'.format(book_name))
#
#
# chapter_name = 'nihao'
# content = 'nihao'
#
# try:
#     # 查询章节名称是否存在章节内容表里面
#     select_table4 = "SELECT chapter_name FROM hw_chinaguji_content"
#     cursor.execute(select_table4)
#     result = cursor.fetchall()
#
#     bookchapter_list = []
#     for i in result:
#         a = str(i).strip().replace("'", "").replace("(", "").replace(")", "").replace(",", "")
#         bookchapter_list.append(a)
#
#     select_bookname_id = "SELECT bookname_id FROM hw_chinaguji_bookname WHERE bookname='%s'" % (book_name)
#     cursor.execute(select_bookname_id)
#     reault = cursor.fetchone()
#     buji_id = int(str(reault).strip().replace(",", "").replace("(", "").replace(")", ""))
#
#     if book_name not in bookchapter_list:
#         sql_insert_chaptercontent = "INSERT INTO hw_chinaguji_content(chapter_name, chapter_content, relation_bookname_id) VALUES('%s', '%s', '%d')" % (chapter_name, content, buji_id)
#         cursor.execute(sql_insert_chaptercontent)
#         print('{} 章节内容插入成功'.format(book_name))
# except:
#     print('{} 章节内容插入失败'.format(book_name))
#
# db.commit()
# cursor.close()
# db.close()



