# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AihrItem(scrapy.Item):
    # 岗位名称
    postName = scrapy.Field()
    # 公司名称
    companyName = scrapy.Field()
    # 薪资
    salary = scrapy.Field()
    # 工作地址
    address = scrapy.Field()
    #创建时间
    createTime = scrapy.Field()

class MasterItem(scrapy.Item):
    url = scrapy.Field()


class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #公司名称
    name = scrapy.Field()
    #公司性质
    nature =scrapy.Field()
    #公司规模
    scale =scrapy.Field()
    #公司网站
    website =scrapy.Field()
    #公司行业
    industry = scrapy.Field()
    #公司地址
    address = scrapy.Field()
    # 公司介绍
    describe = scrapy.Field()
    # 来源(网址)
    source = scrapy.Field()
    # 创建时间
    createTime = scrapy.Field()

class QcwyPostItem(scrapy.Item):
    # 岗位名称
    postName = scrapy.Field()
    # 公司名称
    companyName = scrapy.Field()
    # 工作经验
    experience = scrapy.Field()
    # 最低学历
    education = scrapy.Field()
    # 招聘人数
    number = scrapy.Field()
    # 发布日期
    releaseDate = scrapy.Field()
    # 公司福利
    welfare = scrapy.Field()
    # 职位描述
    postDescribe = scrapy.Field()
    # 工作地址
    address = scrapy.Field()
    # 职位类别
    category = scrapy.Field()
    # 薪
    salary = scrapy.Field()
    #部门信息
    department = scrapy.Field()

class QcwyCompanyItem(scrapy.Item):
    # 公司名称
    name = scrapy.Field()
    # # 公司性质
    # nature = scrapy.Field()
    # # 公司规模
    # scale = scrapy.Field()
    # # 公司行业
    # industry = scrapy.Field()
    #公司情况信息
    info = scrapy.Field()
    # 公司介绍
    describe = scrapy.Field()
    # 公司地址
    address = scrapy.Field()