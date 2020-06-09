import requests
import scrapy


class BlogSpider(scrapy.Spider):
    name = 'seloger'
    start_urls = "https://www.seloger.com/list.htm?projects=2,5&types=1,2&natures=1,2,4&places=[{cp:75}]&price=NaN/1200&rooms=3&enterprise=0&qsVersion=1.0"

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        