import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='hwss', charset='utf8')
cursor = db.cursor()

create_table1_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_bujiclassify (
                    buji_id INT(11) NOT NULL AUTO_INCREMENT COMMENT '部级编号ID',
                    buji_classify_name varchar(80) NOT NULL COMMENT '部级名称',
                    PRIMARY KEY (buji_id),
                    INDEX(buji_id))
                    ENGINE=InnoDB, CHARACTER SET utf8 COLLATE utf8_general_ci;"""

try:
    cursor.execute(create_table1_sql)
    print('部级分类表创建成功')
except:
    print('部级分类表创建失败')


create_table2_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_bookclassify (
                    bookclassify_id INT(11) NOT NULL AUTO_INCREMENT COMMENT '书籍分类编号ID',
                    bookclassify_name VARCHAR (100) NOT NULL COMMENT '书籍分类名称',
                    relation_bujiclassify_id INT(11) NOT NULL COMMENT '关联部级分类编号ID',
                    PRIMARY KEY (bookclassify_id),
                    FOREIGN KEY(relation_bujiclassify_id) REFERENCES hw_chinaguji_bujiclassify(buji_id) on delete cascade on update cascade)
                    ENGINE=InnoDB CHARACTER SET utf8 COLLATE utf8_general_ci;"""

try:
    cursor.execute(create_table2_sql)
    print('书籍分类表创建成功')
except:
    print('书籍分类表创建失败')


create_table3_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_bookname (
                    bookname_id INT(11) NOT NULL AUTO_INCREMENT COMMENT '书籍编号ID',
                    bookname VARCHAR (200) NOT NULL COMMENT '书籍名称',
                    relation_classify_id INT(11) NOT NULL COMMENT '关联书籍分类编号ID',
                    PRIMARY KEY (bookname_id),
                    FOREIGN KEY(relation_classify_id) REFERENCES hw_chinaguji_bookclassify(bookclassify_id) on delete cascade on update cascade)
                    ENGINE=InnoDB CHARACTER SET utf8 COLLATE utf8_general_ci;"""

try:
    cursor.execute(create_table3_sql)
    print('书籍名称表创建成功')
except:
    print('书籍名称表创建失败')


create_table4_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_content (
                    content_id INT(11) NOT NULL AUTO_INCREMENT COMMENT '章节内容编号ID',
                    chapter_name VARCHAR (300) NOT NULL COMMENT '章节名称',
                    chapter_content LONGTEXT NOT NULL COMMENT '章节内容',
                    relation_bookname_id INT(11) NOT NULL COMMENT '关联书籍编号ID',
                    PRIMARY KEY (content_id),
                    FOREIGN KEY(relation_bookname_id) REFERENCES hw_chinaguji_bookname(bookname_id) on delete cascade on update cascade)
                    ENGINE=InnoDB CHARACTER SET utf8 COLLATE utf8_general_ci;"""

try:
    cursor.execute(create_table4_sql)
    print('章节内容表创建成功')
except:
    print('章节内容表创建失败')