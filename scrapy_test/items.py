# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ShopItem(scrapy.Item):
    storeSeq = scrapy.Field(serializer=str)
    ageNames = scrapy.Field()
    appHit = scrapy.Field()
    cateNames = scrapy.Field()
    description = scrapy.Field()
    webUrl = scrapy.Field()
    storeName = scrapy.Field()
    storeGender = scrapy.Field()
    webProdUrl = scrapy.Field()