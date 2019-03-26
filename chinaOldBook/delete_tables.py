import pymysql

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


