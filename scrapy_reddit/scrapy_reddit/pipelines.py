# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time, datetime
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class ScrapyRedditPipeline(object):
    def process_item(self, item, spider):
        time_max = int(time.mktime(datetime.datetime.strptime(settings['IMAGE_DATE_MAX'], "%m/%d/%Y").timetuple()))

        item['title'] = ''.join(item['title']).upper()
        #Filter by score
        if int(item['data_score'][0]) < settings['IMAGE_SOCRE_MIN']:
            raise DropItem('Score is %d, below %d' % (int(item['data_score'][0]), settings['IMAGE_SOCRE_MIN']))
        #Filter by date
        elif int(item['data_timestamp'][0])/1000 > time_max:
            time_str = datetime.datetime.fromtimestamp(int(item['data_timestamp'][0])/1000).strftime('%m/%d/%Y %H:%M:%S')
            raise DropItem('Time is %s, drop', time_str)
        else:
            return item



