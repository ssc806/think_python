# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_reddit project

BOT_NAME = 'scrapy_reddit'
SPIDER_MODULES = ['scrapy_reddit.spiders']
NEWSPIDER_MODULE = 'scrapy_reddit.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

#The downloaded images will put into this directory
IMAGES_STORE = 'images/'
# 90 days of delay for image expiration
IMAGES_EXPIRES = 90
#Log name
FEED_URI = 'logs/%(name)s/%(time)s.csv'
#Log format
FEED_FORMAT = 'csv'

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 100,
    'scrapy_reddit.pipelines.ScrapyRedditPipeline': 300,
}

#Only download the iamges with score above this value
IMAGE_SOCRE_MIN = 20

#Only download the the images with size below this value (M)
#IMAGE_SIZE_MAX = 2

#Only download the images before this time
IMAGE_DATE_MAX = '6/20/2017'