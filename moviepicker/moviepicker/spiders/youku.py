import scrapy
from moviepicker.items import MovieFirstItem


class YoukuSpider(scrapy.Spider):
    name = 'youku'
    allowed_domains = ['youku.com']
    start_urls = ['https://youku.com/category/page/']

    def __init__(self):
        super().__init__()
        self.page = 1

    def start_requests(self):
        url = 'https://youku.com/category/page'
        yield scrapy.FormRequest(
            url=url,
            method='POST',
            formdata={
                'c': '96',
                's': '2',
                'pt': '1',
                'type': 'show',
                'p': str(self.page),
            }
        )

    def parse(self, response):
        print(response.json())
        # for movie in response.json()['data']['list']:
        #     item = MovieFirstItem()
        #     item['name'] = movie['title']
        #     item['site'] = 'BILIBILI'
        #
        #     yield item
        #
        # if response.json()['data']['has_next'] == 1:
        #     self.page += 1
        #     url = self.url_template % self.page
        #     yield scrapy.Request(url)
