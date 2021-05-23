import scrapy
from moviepicker.items import MovieFirstItem


class BilibilidocumentarySpider(scrapy.Spider):
    name = 'bilibilidocumentary'
    allowed_domains = ['api.bilibili.com']
    start_urls = []

    def __init__(self):
        self.page = 1
        self.url_template = 'https://api.bilibili.com/pgc/season/index/result?st=3&producer_id=-1&style_id=-1&release_date=-1&season_status=1&order=2&sort=0&page=%d&season_type=3&pagesize=20&type=1'
        BilibilidocumentarySpider.start_urls.append(self.url_template % self.page)
        super().__init__()

    def parse(self, response):
        for movie in response.json()['data']['list']:
            item = MovieFirstItem()
            item['name'] = movie['title']
            item['site'] = 'BILIBILI'

            yield item

        if response.json()['data']['has_next'] == 1:
            self.page += 1
            url = self.url_template % self.page
            yield scrapy.Request(url)
