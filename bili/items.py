# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    tname = scrapy.Field()
    bvidnum = scrapy.Field()
    aid = scrapy.Field()
    like = scrapy.Field()
    coin = scrapy.Field()
    favorite = scrapy.Field()
    share = scrapy.Field()
    name = scrapy.Field()
    dynamic = scrapy.Field()
    view=scrapy.Field()
    danmu=scrapy.Field()
    his_rank=scrapy.Field()
    reply=scrapy.Field()
