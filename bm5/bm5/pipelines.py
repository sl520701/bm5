# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
class Bm5Pipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'image2')#join是将括号里组成一个含路径和文件名的文件，dirname是去掉文件名，返回路径
        if not os.path.exists(self.path):
            os.mkdir(self.path)
    def process_item(self, item, spider):
        category = item['category']
        urls = item ['image_urls']
        category_path = os.path.join(self.path,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            image_name = url.split('__')[-1]
            request.urlretrieve(url,os.path.join(category_path,image_name))
        return item