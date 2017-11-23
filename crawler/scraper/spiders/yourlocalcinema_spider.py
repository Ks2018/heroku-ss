# import scrapy

# not used currently


# class YourLocalCinemaSpider(scrapy.Spider):
#
#     name = 'yourlocalcinema'
#
#     def start_requests(self):
#         urls = [
#             'http://www.yourlocalcinema.com/crouchend.html'
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         for title in response.xpath("//*[@id='wrapper']/div/div/p"):
#             yield {
#                 'movie/cinema': title.css('*::text').extract(),
#                 'cinema/time': title.css('p::text').extract(),
#                 'location/none': title.css('strong::text').extract()
#             }
