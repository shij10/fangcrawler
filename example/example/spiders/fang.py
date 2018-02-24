# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FangSpider(CrawlSpider):
    name = 'fang'
    allowed_domains = ['esf.cd.fang.com']
    start_urls = ['http://esf.cd.fang.com/']

    rules = (
        Rule(LinkExtractor(allow=r'chushou/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        print 'hello world'
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
