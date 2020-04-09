# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import pymysql
import os
class BiliPipeline(object):
    def __init__(self):
        if os.path.exists('bilili.csv'):
            self.f=open('bilili.csv','a',encoding='utf-8-sig',newline='')
            self.w=csv.writer(self.f)
        else:
            self.f = open('bilili.csv', 'a', encoding='utf-8-sig', newline='')
            self.w = csv.writer(self.f)
            self.w.writerow(['标题', '视频简介', '分类', 'bv号', 'av号', '播放量', '弹幕数', '最高全站日排行', '点赞', "硬币", "收藏", "分享", 'up主', '标签'])

        # self.con = pymysql.connect("ip", "user", "password", port=10251)
        # self.cursor = self.con.cursor()

    def process_item(self, item, spider):
        self.w.writerow([item['title'], item['desc'], item['tname'],item['bvidnum'], item['aid'],item['view'],item['danmu'],item['his_rank'],item['like'], item['coin'], item['favorite'], item['share'], item['name'], item['dynamic']])
        # sql = '''INSERT INTO `B站`.`key_Search`(`标题`,`视频简介`,`分类`,`bv号`,`av号`,`播放量`,`弹幕数`,`最高全站日排行`,`点赞`, `硬币`, `收藏`, `分享`,`up主`,`标签`) VALUES (%s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        # value = (item['title'], item['desc'], item['tname'],item['bvidnum'], item['aid'],item['view'],item['danmu'],item['his_rank'],item['like'], item['coin'], item['favorite'], item['share'], item['name'], item['dynamic'])
        # self.cursor.execute(sql, value)
        # self.con.commit()
        return item

    def spider_close(self,spider):
        print('ok')
        self.f.close()
        # self.con.close()
