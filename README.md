# MoviePicker

## Dependence Package
* `scrapy-fake-useragent` for random User-Agent generator

## Data Dictionary
* Movie First Item
    1. Name (ID)
    2. Site
        * IQIYI
          * URL: `https://pcw-api.iqiyi.com/search/recommend/list?channel_id=1&data_type=1&is_purchase=0&mode=24&page_id=2&ret_num=48`
            * channel_id=1
           * data_type=1
            * is_purchase=0
            * mode=24
            * page_id=2
            * ret_num=48
          * response
            * albumName
            * name
            * title
        * QQ
        * YOUKU
        * MIGU
        * XIGUA
        * BILIBILI
* Movie
    1. Name (ID)
    2. Site (List)
    3. Score (List)
    