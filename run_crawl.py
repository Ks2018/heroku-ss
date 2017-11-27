from scrapy.crawler import CrawlerProcess
from crawler.scraper.spiders.picturehouse_spider import PictureHouseSpider
from scrapy.utils.project import get_project_settings
import django

django.setup()

process = CrawlerProcess(get_project_settings())

process.crawl(PictureHouseSpider)
process.start()