import scrapy


class SubtitledscreeningsItem(scrapy.Item):
    date = scrapy.Field()
    movie = scrapy.Field()
    time = scrapy.Field()
    age = scrapy.Field()
    pass
