
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from scrapy_reddit.items import ScrapyRedditItem


class RedditSpider(CrawlSpider):
    #The crawl name
    name = 'reddit'

    #If you don't set allowed_domains then all domains are allowed by default. 
    allowed_domains = ["www.reddit.com"]

    start_urls = [
        'http://www.reddit.com/r/pics'
    ]

    rules = [
        Rule(LinkExtractor(
            allow=['/r/pics/\?count=\d*&after=\w*']),
            callback='parse_item',
            follow=True)
    ]

    def parse_item(self, response):
        
        selector_list = response.css('div.thing')

        for selector in selector_list:
            item = ScrapyRedditItem()
            item['image_urls'] = selector.xpath('a/@href').extract()
            item['title'] = selector.xpath('div/p/a/text()').extract()
            item['url'] = selector.xpath('a/@href').extract()
            item['data_score'] = selector.xpath('@data-score').extract()
            item['data_timestamp'] = selector.xpath('@data-timestamp').extract()

            yield item
    
    