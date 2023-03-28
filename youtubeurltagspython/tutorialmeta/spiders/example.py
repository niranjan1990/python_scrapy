





# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

class ExampleSpider(scrapy.Spider):
    name = 'example'
    #start_urls = ['https://apnews.com/article/health-education-lawsuits-connecticut-yale-university-6e2cf430ef0c14c45ff064f07e5d5c4a',
    #               'https://www.nytimes.com/']

    def start_requests(self):
        df = pd.read_csv('~/Downloads/news.csv')

        urls = df['url']
        #print('url',urls)
        
        for url in urls:
            #print('url',url)
            if 'https' in url:
                #print('ifurl',url)
                yield scrapy.Request(url=url, callback=self.parse)
                
    def parse(self, response):
        address = response.url
        count_address = len(address)
        content_type = response.headers['Content-Type'] 
        status_code = response.status     
        title = response.xpath("//title/text()").extract()
        count_title = len(title[0])
        description = response.xpath("//meta[@name='description']/@content").extract_first()
        count_description = len(description) if description else 0
        keywords = response.xpath("//meta[@name='keywords']/@content").extract_first()
        h1 = response.xpath('//h1//text()').extract_first()
        h2 = response.xpath('//h2//text()').extract_first()
        robot = response.xpath("//meta[@name='robots']/@content").extract_first()
        download_time = response.meta['download_latency']
        image = response.xpath("//meta[@property='og:image']/@content").extract_first()
        yield {
            'Address': address,
            #'Address count': count_address,
            #'Content Type': content_type,
            #'Status code': status_code,
            'Title': title,
            #'Title count': count_title,
            #'Meta description': description,
            #'Meta description count': count_description,
            #'Meta keywords': keywords,
            #'H1': h1,
            #'H2': h2,
            #'Robot': robot,
            #'Download time': download_time,
            'Image': image,
        }