import scrapy


class CollegeSpider(scrapy.Spider):
    name = "college"

    def start_requests(self):
        urls = [
            'https://www.prepscholar.com/sat/s/colleges/Appalachian-State-University-SAT-scores-GPA',
            'https://www.prepscholar.com/sat/s/colleges/ASU-SAT-scores-GPA',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        collegeName = response.css('#twocolumns h1::text').extract()
        description = response.css('#twocolumns .content-holder #content .siteBlock .siteBlockContent .heading-head h2::text').extract()
        #date = response.css('.filter-items__results-item div:nth-of-type(1) time::text').extract()
        #print ('response',description,date)
        print ("_______________________________________")
        print ('collegeName',collegeName)
        print ('description',description)
        for item in zip(collegeName,description):
			scraped_info = {
				'collegeName' : item[0],
				'description' : item[1], 
			}
			print (scraped_info)
			print ("_______________________________________")

        
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)