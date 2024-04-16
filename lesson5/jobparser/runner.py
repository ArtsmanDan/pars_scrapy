from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from jobparser.spiders.hhru import HhruSpider
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging

if __name__ == '__main__':
    configure_logging()
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    # Создание процесса краулера с настройками проекта
    process = CrawlerProcess(get_project_settings())

    # Добавление паука в процесс
    process.crawl(HhruSpider)

    # Запуск процесса (блокирующий вызов, будет работать, пока не завершится краулер)
    process.start()
