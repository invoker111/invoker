# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

db = pymysql.connect(
    '127.0.0.1',
    'root',
    '1607439239',
    'mystorage',
    charset='utf8mb4'
)

cursor = db.cursor()

# # 删除并新建表
# cursor.execute('drop table if exists zhi;')
#
# cursor.execute('create table zhi(id int(10) not null ,title varchar(1000) not null, best_answer TEXT(30000) not null, answers TEXT(30000) not null, word varchar(1000) not null);')


# 导入数据库
class SpiPipeline(object):
    def __init__(self):
        self.id = 1

    def process_item(self, item, spider):
        sql = "insert into zhi(id,title,best_answer,answers,word) select '%d','%s','%s','%s','%s' from dual where not exists(select title,best_answer,answers from zhi where title='%s' and best_answer='%s' and answers='%s');" % (self.id, pymysql.escape_string(item['title']), pymysql.escape_string(item['best_answer']), pymysql.escape_string(item['answers']), pymysql.escape_string(item['word']), pymysql.escape_string(item['title']), pymysql.escape_string(item['best_answer']), pymysql.escape_string(item['answers']))
        cursor.execute(sql)
        self.id += 1
        db.commit()
