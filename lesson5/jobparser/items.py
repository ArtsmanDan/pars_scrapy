# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    url_vacancy = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    experience = scrapy.Field()
    employment = scrapy.Field()
    accept_temporary = scrapy.Field()
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    company_rating = scrapy.Field()
    company_review_count = scrapy.Field()
    location = scrapy.Field()
    vacancy_description = scrapy.Field()
