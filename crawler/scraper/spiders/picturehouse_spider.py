import scrapy


class CrouchEndPictureHouseSpider(scrapy.Spider):

    name = 'Crouch End Picturehouse'

    def start_requests(self):
        urls = [
            "https://www.picturehouses.com/cinema/Crouch_End_Picturehouse/Whats_On"  # noqa: E501
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for movie in response.xpath("//*[@id='main']/div[2]/div/ul/li"):
            yield {
                'date': movie.css('.dark::text').extract(),
                'title': movie.css('.top-mg-sm a::text').extract(),
                'time': movie.css('.col-xs-10 a::text').extract(),
            }
