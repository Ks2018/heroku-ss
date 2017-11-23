BOT_NAME = 'subtitledscreenings'

SPIDER_MODULES = ['scrapy.scraper.spiders']
NEWSPIDER_MODULE = 'scrapy.scraper.spiders'

# Output to JSON for testing scraping output
FEED_URI = "tmp/output.json"
FEED_FORMAT = "json"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'scrapy.scraper.scrapepipeline.ScrapePipeline': 300,
    'scrapy.scraper.databasepipeline.DatabasePipeline': 800,
}
