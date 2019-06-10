# -*- coding: utf-8 -*-
import scrapy
from bm5.items import Bm5Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib import request

class BmSpider(CrawlSpider):
    name = 'bm'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']
    rules = (
        Rule(LinkExtractor(allow='https://car.autohome.com.cn/pic/series/65.+'),callback='parse_page',follow=True),)
    def parse_page(self, response):
        #selectorlist - list
        category = response.xpath("//div[@class='uibox']/div[@class='uibox-title']/text()").get()
        urls = response.xpath('//ul/li/a/img/@src').getall()
        urls = list(map(lambda url:response.urljoin(url),urls))
        print(urls)
        srcs = []
        #保存高清图片
        for url in urls:
            url = url.replace('t_','')
            srcs.append(url)
        yield Bm5Item(image_urls=srcs,category = category)

        #保存缩略图
        # uiboxs =response.xpath("//div[@class='column grid-16']/div[@class='uibox']")
        # print(len(uiboxs))
        # for uibox in uiboxs:
        #     category = uibox.xpath("./div[1]/a/text()").get()
        #     print(category)
        #     urls = uibox.xpath('.//ul/li/a/img/@src').getall()
        #     # for url in urls:
        #     #     url = response.urljoin(url)#把这个不带前缀的url变成与之相关可以使用的URL
        #     urls = list(map(lambda url:response.urljoin(url),urls))
        #     print(urls)
        #     item = Bm5Item(category=category,image_urls =urls)
        #     yield item
