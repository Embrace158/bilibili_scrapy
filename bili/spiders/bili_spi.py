# -*- coding: utf-8 -*-
import time

import scrapy
import re
import json
import requests
from ..items import BiliItem

class BiliSpiSpider(scrapy.Spider):
    key = input('关键字:')
    name = 'bili_spi'
    allowed_domains = ['search.bilibili.com']
    start_urls = ['https://search.bilibili.com/all?keyword={}&order=click&duration=0&tids_1=0'.format(key)]
    def parse(self, response):
        hrefs=response.xpath(".//li[@class='video-item matrix']/a/@href").getall()
        for i in range(0,len(hrefs)):
            try:
                item = BiliItem()
                r=re.findall('BV[0-9a-zA-Z]*',hrefs[i])
                url2 = "https://api.bilibili.com/x/web-interface/view?&bvid="+"".join(r)
                yield scrapy.Request(url2,callback=self.second_parse,dont_filter=True)

            except :
                continue
        urls=['https://search.bilibili.com/all?keyword={}&order=click&duration=0&tids_1=0&page={}'.format(str(self.key),str(x)) for x in range(2,51)]
        for urll in urls:
            yield scrapy.Request(url=urll,callback=self.parse)

    def second_parse(self,response):
        item = BiliItem()
        json_data=json.loads(response.text)
        json_Info1 = json_data['data']
        item['bvidnum'] = json_Info1['bvid']
        item['aid'] = json_Info1['aid']
        item['tname'] = json_Info1['tname']
        item['title'] = json_Info1['title']
        item['desc'] = json_Info1['desc']
        own = json_Info1['owner']
        item['name'] = own['name']
        #             print(name)

        # #stat数据
        stat = json_Info1['stat']
        item['view'] = stat['view']
        item['danmu'] = stat['danmaku']
        item['reply'] = stat['reply']
        item['favorite'] = stat['favorite']
        item['coin'] = stat['coin']
        item['share'] = stat['share']
        item['like'] = stat['like']
        item['his_rank'] = stat['his_rank']
        item['dynamic'] = json_Info1['dynamic']
        yield item

