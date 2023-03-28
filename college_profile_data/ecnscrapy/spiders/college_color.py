import scrapy


class ColorSpider(scrapy.Spider):
    name = "color"

    def start_requests(self):
        urls = [
            'https://teamcolorcodes.com/ncaa-color-codes/america-east/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('color',response.css)
        print(response)
        collegeName = response.css('.entry-content .team-button a::text').extract()
        description = response.css('#twocolumns .content-holder #content .siteBlock .siteBlockContent .heading-head h2::text').extract()
        #date = response.css('.filter-items__results-item div:nth-of-type(1) time::text').extract()
        #print ('response',description,date)
        print ("_______________________________________")
       
        for item in zip(collegeName,description):
			scraped_info = {
				'collegeName' : item[0],
				'description' : item[1], 
			}
	print (scraped_info)
	print ("_______________________________________")		
    return(scraped_info)

        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)