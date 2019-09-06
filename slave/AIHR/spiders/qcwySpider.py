import scrapy #导入scrapy包
from scrapy.selector import Selector #选择器
from bs4 import BeautifulSoup
from scrapy.http import Request #一个单独的request模块，需要跟进URL的时候需要用它
from AIHR.items import QcwyPostItem, QcwyCompanyItem#自己定义的需要保存的字段

# 51job（前程无忧）commands
#by dsy
class QcwySpider(scrapy.Spider):
    name = "qcwy"
    allowed_domains = ["51job.com"]
    start_urls = [
        'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&keywordtype=2&curr_page=1&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&dibiaoid=0&confirmdate=9']

    def parse(self, response):
        # 1 爬取列表
        # 获取所有id为resultList的div
        # 不加上extract就还是个选择器
        div_list = response.xpath('//*[@id="resultList"]/div')
        for div_item in div_list:
            posturl = div_item.xpath('string(p/span/a/@href)').extract()[0]
            if posturl:
                # print("********************")
                # print(posturl)
                yield Request(posturl, callback=self.getPostInfo)

        # 2 获取下一页链接
        next_page = response.xpath('//div[@class="p_in"]').extract()
        # 判断nest_page是否为空，则表示是否存在下一页
        if next_page:
            next_url = response.xpath('//div[@class="p_in"]/ul/li[8]/a/@href').extract()
            # print(next_url)
            # extract得到的是一个list列表
            yield Request(url=next_url[0], callback=self.parse)

    def getPostInfo(self, response):
        postitem = QcwyPostItem()

        postName = response.xpath('string(//div[@class="cn"]/h1/text())').extract()[0]
        companyName = response.xpath('string(//div[@class="cn"]/p[1]/a)').extract()[0]
        experience = response.xpath('string(//div[@class="t1"]/span[1]/text())').extract()[0]
        education = response.xpath('string(//div[@class="t1"]/span[2]/text())').extract()[0]
        number = response.xpath('string(//div[@class="t1"]/span[3]/text())').extract()[0]
        releaseDate = response.xpath('string(//div[@class="t1"]/span[4]/text())').extract()[0]

        welfare_list = response.xpath('//p[@class="t2"]/span/text()').extract()
        welfare = ""
        for i in range(len(welfare_list)):
            if not welfare_list[i].strip() == '':
                # print('++++++++++++++++'+welfare_list[i])
                welfare = welfare + welfare_list[i]
                if i != len(welfare_list) - 1:
                    welfare = welfare + ','
        postDescribe_list = response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract()
        postDescribe = ""
        for i in range(len(postDescribe_list)):
            if not postDescribe_list[i].strip() == '':
                # print("+++++++" + postDescribe_list[i])
                postDescribe = postDescribe + postDescribe_list[i]
        address = response.xpath('string(//div[@class="tCompany_main"]/div[3]/div/p)').extract()[0]
        department = response.xpath('string(//div[@class="tCompany_main"]/div[4]/div)').extract()[0]
        category = response.xpath('string(//div[@class="mt10"]/p/span[2])').extract()[0]
        salaryY = response.xpath('string(//div[@class="cn"]/strong)').extract()[0]
        # print(postName, companyName, experience, education, number, releaseDate, welfare, postDescribe, address, department, category, salaryY)
        postitem['postName'] = "".join(postName.split())
        postitem['companyName'] = "".join(companyName.split())
        postitem['experience'] = "".join(experience.split())
        postitem['education'] = "".join(education.split())
        postitem['number'] = "".join(number.split())
        postitem['releaseDate'] = "".join(releaseDate.split())
        postitem['welfare'] = "".join(welfare.split())
        postitem['postDescribe'] = "".join(postDescribe.split())
        postitem['address'] = "".join(address.split())
        postitem['department'] = "".join(department.split())
        postitem['category'] = "".join(category.split())
        postitem['salaryY'] = "".join(salaryY.split())

        companyurl = response.xpath('string(//p[@class="cname"]/a/@href)').extract()[0]
        # print("companyurl = " + companyurl)
        if companyurl:
            yield Request(companyurl, callback=self.getCompanyInfo)
        yield postitem

    def getCompanyInfo(self, response):
        companyitem = QcwyCompanyItem()
        name = response.xpath('string(//div[@class="in img_on"]/h1/text())').extract()[0]
        info = response.xpath('string(//p[@class="ltype"]/text())').extract()[0]
        describe_list = response.xpath('//div[@class="in"]/p/text()').extract()
        describe = ""
        # print('*************')
        # print(len(describe_list))
        for i in range(len(describe_list)):
            if not describe_list[i].strip() == '':
                # print(companyDescribe_list[i])
                describe = describe + describe_list[i]

        address = response.xpath('string(//p[@class="fp"])').extract()[0]
        # print("address = " + address)
        companyitem['name'] = "".join(name.split())
        companyitem['info'] = "".join(info.split())
        companyitem['describe'] = "".join(describe.split())
        companyitem['address'] = "".join(address.split())

        yield companyitem
