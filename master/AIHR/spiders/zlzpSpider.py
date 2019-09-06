# encoding: utf-8
from AIHR.items import AihrItem, CompanyItem, MasterItem #自己定义的需要保存的字段
# 1. 导入RedisCrawlSpider类，不使用CrawlSpider
from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
# 使用redis去重
from scrapy.dupefilters import RFPDupeFilter

#by dsy
class ZlzpSpider(RedisCrawlSpider):
    name = "hyperchain"
    redis_key = 'hyperchain:start_urls'
    item = MasterItem()
    # start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html\?lang\=c\&stype\=\&postchannel\=0000\&workyear\=99\&cotype\=99\&degreefrom\=99\&jobterm\=99\&companysize\=99\&providesalary\=99\&lonlat\=0%2C0\&radius\=-1\&ord_field\=0\&confirmdate\=9\&fromType\=\&dibiaoid\=0\&address\=\&line\=\&specialarea\=00\&from\=\&welfare\=']
    page_lx = LinkExtractor(allow=('https://search.51job.com/list/.*&welfare'))
    # 详情页面
    # self_lx = LinkExtractor(allow=(r'https://jobs.51job.com/foshan-sdq/\d+'))
    # 规则
    rules = (
        Rule(page_lx, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = self.item
        item['url'] = response.url
        return item
