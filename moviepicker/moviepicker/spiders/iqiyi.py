import scrapy
from moviepicker.items import MovieFirstItem


class IqiyiSpider(scrapy.Spider):
    name = 'iqiyi'
    allowed_domains = ['pcw-api.iqiyi.com']
    start_urls = ['https://pcw-api.iqiyi.com/search/recommend/list?channel_id=1&data_type=1&is_purchase=0&mode=24&page_id=%d&ret_num=48']

    def __init__(self):
        self.page = 1
        IqiyiSpider.start_urls[0] = IqiyiSpider.start_urls[0] % self.page
        super().__init__()

    def parse(self, response):
        for movie in response.json()['data']['list']:
            item = MovieFirstItem()
            item['name'] = movie['name']
            item['site'] = 'IQIYI'

            yield item

        if response.json()['data']['has_next'] == 1:
            self.page += 1
            url = 'https://pcw-api.iqiyi.com/search/recommend/list?channel_id=1&data_type=1&is_purchase=0&mode=24&page_id=%d&ret_num=48' % self.page
            yield scrapy.Request(url)
