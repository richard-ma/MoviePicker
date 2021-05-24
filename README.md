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
          * URL: `https://api.bilibili.com/pgc/season/index/result?area=-1&style_id=-1&release_date=-1&season_status=1&order=6&st=2&sort=0&page=1&from_spmid=666.7&season_type=2&pagesize=20&type=1`
            * area=-1
            * style_id=-1
            * release_date=-1
            * season_status=1
            * order=6
            * st=2
            * sort=0
            * page=1
          * response
            * title
          * URL: `https://api.bilibili.com/pgc/season/index/result?st=3&producer_id=-1&style_id=-1&release_date=-1&season_status=1&order=2&sort=0&page=1&season_type=3&pagesize=20&type=1`
            * producer_id=-1
            * style_id=-1
            * release_date=-1
            * season_status=1
            * order=2
            * st=2
            * sort=0
            * page=1
            * pagesize=20
          * response
            * title
            
* Movie
    1. Name (ID)
    2. Site (List)
    3. Score (List)
    
## Douban API
* URL: `https://movie.douban.com/j/subject_suggest?q=[keyword]`
    * q=\[keyword\]
* response
    * title
    * url
    * year
    * id [douban_id]
* URL: `https://movie.douban.com/subject/[movie_id]/`
    * `<strong class="ll rating_num" property="v:average">7.6</strong>`
    