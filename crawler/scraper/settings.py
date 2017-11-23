BOT_NAME = 'subtitledscreenings'

SPIDER_MODULES = ['crawler.scraper.spiders']
NEWSPIDER_MODULE = 'crawler.scraper.spiders'

# Output to JSON for testing scraping output
FEED_URI = "tmp/output.json"
FEED_FORMAT = "json"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'crawler.scraper.scrapepipeline.ScrapePipeline': 300,
    'crawler.scraper.databasepipeline.DatabasePipeline': 800,
}
