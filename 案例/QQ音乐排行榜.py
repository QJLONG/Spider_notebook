import pymysql
import requests
from lxml import etree


def get_html(url):
    resp = requests.get(url)
    return resp.text


def parse_html(html):
    tree = etree.HTML(html)
    lis = tree.xpath("//ul[@class='songlist__list']/li")
    result = []
    id = 1
    for li in lis:
        song_name = li.xpath("./div/div[@class='songlist__songname']/span/a[2]/@title")[0]
        singer_name = li.xpath("./div/div[@class='songlist__artist']/a/text()")[0]
        result.append((id, song_name, singer_name))
        id += 1
    return result


def save_to_database(data):
    # 连接数据库
    mydb = pymysql.connect(host="localhost",
                           user="hummer",
                           password="747759",
                           database="song_test")
    cursor = mydb.cursor()
    # 创建表的语句
    create_table = """CREATE TABLE song_table(id int(4),song_name varchar(40),singer_name varchar(40))"""
    # 插入数据的语句
    insert = """INSERT INTO song_table values (%s,%s,%s)"""
    cursor.execute(create_table)
    mydb.commit()
    # 遍历每个数据元组，向数据库中插入数据
    for i in data:
        cursor.execute(insert, i)
    mydb.commit()


def select_from_database():
    mydb = pymysql.connect(host="localhost",
                           user="hummer",
                           password="747759",
                           database="song_test")
    cursor = mydb.cursor()
    select = """SELECT * FROM song_table"""
    cursor.execute(select)
    results = cursor.fetchall()
    for result in results:
        print('id: %.2d\t\tsong_name: %.18s\t\tsinger_name: %.6s' % (result[0], result[1], result[2]))


if __name__ == '__main__':
    html = get_html("https://y.qq.com/n/ryqq/toplist/26")
    data = parse_html(html)
    # save_to_database(data)
    select_from_database()