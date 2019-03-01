import scrapy
from douban.items import DoubanItem
class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = []
    for i in range(10):
        start_urls.append( "https://movie.douban.com/top250?start=" + str(i * 25))
    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//*[@id="content"]/div/div[1]/ol/li')
        items = []
        for site in sites:
            item = DoubanItem()
            item['movie_name'] = site.xpath('div/div[2]/div[1]/a/span[1]/text()').extract()
            item['movie_author'] = site.xpath('div/div[2]/div[2]/p[1]/text()[1]').extract()
            item['movie_link'] = site.xpath('div/div[2]/div[1]/a/@href').extract()
            items.append(item)
        return items