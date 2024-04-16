# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import re


def format_salary(list_salary: list):
    # salaries = [doc['salary'] for doc in list_salaries]
    print()
    # salaries = list_salaries
    # for list_item in salaries:
    # убираем пробелы лишние символы
    list_salary = [x.strip().replace('\xa0', '') for x in list_salary]
    print()
    min_salary = None
    max_solary = None
    comment = None
    currency = None
    if len(list_salary) > 0:
        element = 'от'
        try:
            index_min = list_salary.index(element)
            min_salary = list_salary[index_min + 1]
        except ValueError:
            min_salary = None

        element = 'до'
        try:
            index_max = list_salary.index(element)
            max_solary = list_salary[index_max + 1]
        except ValueError:
            max_solary = None
        comment = list_salary[-1]
        currency = list_salary[-3]
    return min_salary, max_solary, comment, currency


class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27018)
        self.mongo_base = client.vacancies12042023

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        id_v = item.get('url_vacancy')
        item['_id'] = re.split(r'[?/]', id_v)[4]
        min_salary, max_solary, comment, currency = format_salary(item.get('salary'))
        item['salary'] = {'min_salary': min_salary, 'max_solary': max_solary, 'comment': comment, 'currency': currency}
        print(item.get('salary'))
        collection.insert_one(item)
        return item
