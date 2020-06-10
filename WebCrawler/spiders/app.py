import requests
import scrapy


class BlogSpider(scrapy.Spider):
    name = 'seloger'



    def start_requests(self):
        start_urls = "https://www.seloger.com/list.htm?projects=2,5&types=1,2&natures=1,2,4&places=[{cp:75}]&price=NaN/1200&rooms=3&enterprise=0&qsVersion=1.0"
    
        # Set the headers here. The important part is "application/json"
        headers =  {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        yield scrapy.http.Request(start_urls, headers=headers)


    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}