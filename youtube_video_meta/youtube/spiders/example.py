# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
#from scrapy import log
from scrapy.cmdline import execute
from scrapy.utils.markup import remove_tags
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

import time

#define spider
class ExampleSpider(scrapy.Spider):
	name = 'example'
	#allowed_domains = ["https://www.youtube.com"]
	start_urls = ['https://www.youtube.com/watch?v=TPYPmsnm44Q']
	#time.sleep(10)

	custom_settings = {
        'DEPTH_LIMIT': '100',
	}
#selectors
	def parse(self, response):
		SET_SELECTOR = '#page-container'
                print(response.css,'title youtube')
		#NEW_SELECTOR = '#watch-header'
		for youtube in response.css(SET_SELECTOR,):

			TITLE_SELECTOR = 'meta ::attr(content)'
			LINK_SELECTOR = 'link ::attr(href)'
			VIEWCOUNT_SELECTOR = '//*[@id="watch7-views-info"]/div[1]/text()'
			DATEPUB_SELECTOR = '//*[@id="watch7-content"]/meta[14]/@content'
			GENRE_SELECTOR = '//*[@id="watch7-content"]/meta[15]/@content'
			NAME_SELECTOR = '//*[@id="watch7-user-header"]/div/a/text()'
			SUBS_SELECTOR = '//*[@id="watch7-subscription-container"]/span/span[1]/text()'
			LIKES_SELECTOR = '//*[@id="watch8-sentiment-actions"]/span/span[1]/button/span/text()'
			DISLIKES_SELECTOR = '//*[@id="watch8-sentiment-actions"]/span/span[3]/button/span/text()'
			#COMMENT_SELECTOR = '//*[@id="comment-section-renderer"]/text()'
			