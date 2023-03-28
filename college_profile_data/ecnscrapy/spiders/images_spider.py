import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"

    def start_requests(self):
        urls = [
           'https://www.insidehighered.org',
           'https://www.browndailyherald.com/',
           'https://www.insidehighered.com/',
           'https://www.washingtonpost.com/education/2020/09/17/college-applicants-will-make-pandemic-focus-their-admissions-essays-should-they',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
    
        description = response.xpath("//meta[@property='og:image']/@content").extract_first()
        i=0
        if description == None:
            i +=1
            print('total count', i)
        else:
            print ("_________________image link______________________")
            print (description)
            print ("_______________________________________")
       
        
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)