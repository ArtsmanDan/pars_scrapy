import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://hh.ru/search/vacancy?from=suggest_post&hhtmFrom=main&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true&experience=noExperience&schedule=remote&text=Python"]

    def parse(self, response: HtmlResponse, **kwargs):
        next_page = response.xpath('//a[@data-qa="pager-next"]/@href').get()
        # print(next_page)
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath('//span[@class="serp-item__title-link-wrapper"]//a/@href').getall()
        # print(len(links), response.status, response.url)
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        print()
        url_vacancy = response.url
        name = response.xpath('//h1/text()').get()
        salary = response.xpath('//span[@data-qa="vacancy-salary-compensation-type-net"]//text()').getall()
        experience = response.xpath('//span[@data-qa="vacancy-experience"]//text()').getall()
        employment = response.xpath('//p[@data-qa="vacancy-view-employment-mode"]//text()').getall()
        accept_temporary = response.xpath('//p[@data-qa="vacancy-view-accept-temporary"]//text()').getall()
        company_name = response.xpath('//a[@data-qa="vacancy-company-name"]//text()').getall()
        company_url = response.xpath('//a[@data-qa="vacancy-company-name"]/@href').get()
        company_rating = response.xpath('//div[@data-qa="employer-review-small-widget-total-rating"]/text()').get()
        company_review_count = response.xpath('//div[@data-qa="employer-review-small-widget-review-count-action"]//text()').get()
        location = response.xpath('//p[@data-qa="vacancy-view-location"]/text()').get()
        # оставляю теги для сохранения оформления
        vacancy_description = response.xpath('//div[@data-qa="vacancy-description"]').getall()
        yield JobparserItem(
            url_vacancy=url_vacancy,
            name=name,
            salary=salary,
            experience=experience,
            employment=employment,
            accept_temporary=accept_temporary,
            company_name=company_name,
            company_url=company_url,
            company_rating=company_rating,
            company_review_count=company_review_count,
            location=location,
            vacancy_description=vacancy_description
        )

        print()
# //span[@class="serp-item__title-link-wrapper"]/a
# //h2//a/@href
# //a[@data-qa="pager-next"]