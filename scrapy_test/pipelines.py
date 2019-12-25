# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyTestPipeline(object):
    def process_item(self, item, spider):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        return item

    def open_spider(self, spider):
        print('open_spider')

    def close_spider(self, spider):
        print('close_spider')