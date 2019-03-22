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

# delete_table = "DROP TABLE hw_chinaguji_bujiclassify"
# try:
#     cursor.execute(delete_table)
#     print('删除部级分类表成功')
# except:
#     print('删除部级分类表失败')

create_table1_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_bujiclassify (
                    id INT NOT NULL AUTO_INCREMENT,
                    buji_classify_name varchar(80) NOT NULL,
                    PRIMARY KEY (id))
                    ENGINE=InnoDB, DEFAULT CHARSET=utf8
                    """
try:
    cursor.execute(create_table1_sql)
    print('部级分类表创建成功')
except:
    print('部级分类表创建失败')

create_table2_sql = """CREATE TABLE IF NOT EXISTS hw_chinaguji_twoclassify (
                    id INT NOT NULL AUTO_INCREMENT,
                    twoclassify_name VARCHAR (100) NOT NULL,
                    relation_table1_id INT NOT NULL ,
                    PRIMARY KEY (id))
                    ENGINE=InnoDB, DEFAULT CHARSET=utf8
                    """
try:
    cursor.execute(create_table2_sql)
    print('书籍分类表创建成功')
except:
    print('书籍分类表创建失败')



