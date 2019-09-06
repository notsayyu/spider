# encoding: utf-8
import datetime
import scrapy #导入scrapy包
from scrapy.selector import Selector #选择器
from bs4 import BeautifulSoup
from scrapy.http import Request #一个单独的request模块，需要跟进URL的时候需要用它
from AIHR.items import AihrItem, CompanyItem, MasterItem #自己定义的需要保存的字段
# 1. 导入RedisCrawlSpider类，不使用CrawlSpider
from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
# 使用redis去重
from scrapy.dupefilters import RFPDupeFilter
from redis import Redis

#by dsy
class ZlzpSpider(CrawlSpider):
    name = "slave"
    redis_key = 'dsy:start_urls'

    # def parse(self, response):
    #     res = Selector(response)
    #     # body_list = res.xpath('/html/body').extract()
    #     #1 爬取列表
    #     #获取所有class为newlist的table
    #     #不加上extract就还是个选择器
    #     table_newlist = res.xpath('//*[@id="resultList"]/div')
    #     for table_item in table_newlist:
    #         posturl = table_item.xpath('string(p/span/a/@href)').extract()[0]
    #         if posturl:
    #             print("********************")
    #             print(posturl)
    #             yield Request(posturl, callback=self.getPostInfo)
    #
    #     #2 获取下一页链接
    #     next_page = res.xpath('//div[@class="p_in"]').extract()
    #     #判断nest_page是否为空，则表示是否存在下一页
    #     if next_page:
    #         next_url = res.xpath('//div[@class="p_in"]/ul/li[8]/a/@href').extract()
    #         print("====")
    #         #extract得到的是一个list列表
    #         yield Request(url=next_url[0], callback=self.parse)

    def parse(self, response):
        postitem = AihrItem()
        postName = response.xpath('string(//div[@class="cn"]/h1/text())').extract()[0]
        companyName = response.xpath('string(//div[@class="cn"]/p[1]/a)').extract()[0]
        salary = response.xpath('string(//div[@class="cn"]/strong)').extract()[0]
        address = response.xpath('string(//div[@class="cn"]/p[2]/text())').extract()[0]
        createTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在

        postitem['postName'] = "".join(postName.split())
        postitem['companyName'] = "".join(companyName.split())
        postitem['salary'] = "".join(salary.split())
        postitem['address'] = "".join(address.split())
        postitem['createTime'] = "".join(createTime.split())

        print(postitem)
        yield postitem


