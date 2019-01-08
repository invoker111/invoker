# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiItem(scrapy.Item):
    # define the fields for your item here like:
    # #############爬取内容字典##################
    id = scrapy.Field()
    next_page = scrapy.Field()
    title = scrapy.Field()
    main = scrapy.Field()
    best_answer = scrapy.Field()
    answers = scrapy.Field()
    word = scrapy.Field()
