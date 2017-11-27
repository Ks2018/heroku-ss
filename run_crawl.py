from scrapy.crawler import CrawlerProcess
from crawler.scraper.spiders.crouch_end_ph import CrouchEndPictureHouseSpider
from scrapy.utils.project import get_project_settings
import django

django.setup()

process = CrawlerProcess(get_project_settings())

process.crawl(CrouchEndPictureHouseSpider)
process.start()
