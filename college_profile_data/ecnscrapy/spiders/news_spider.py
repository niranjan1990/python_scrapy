import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"

    def start_requests(self):
        urls = [
            'https://www.astrazeneca.com/media-centre/press-releases.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        description = response.css('.filter-items__results-item div:nth-of-type(1) h3::text').extract()
        date = response.css('.filter-items__results-item div:nth-of-type(1) time::text').extract()
        #print ('response',description,date)
        print ("_______________________________________")

        for item in zip(description,date):
			scraped_info = {
				'description' : item[0],
				'date' : item[1],
			}
            
			print (scraped_info)
			print ("_______________________________________")

        
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)