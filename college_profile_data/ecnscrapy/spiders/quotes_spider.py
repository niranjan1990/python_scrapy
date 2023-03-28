import scrapy
import csv


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    your_list = list()

    with open('profile.csv', 'r') as f:
        reader = csv.reader(f)
        for line_list in reader:
            your_list.append(line_list[11])
    start_urls = your_list
    print(start_urls)

    def parse(self, response):
        image = response.css('#main .uprofile_dis_wrap_outer .user_img_wrap img::attr(src)').extract()
        name = response.css('#main .uprofile_dis_wrap_outer .uprofile_dis_wrap h3::text').extract()
        company = response.xpath('//*[@id="main"]/div/div[2]/div[1]/div[2]/div/label[1]').extract()
        phone = response.xpath('//*[@id="main"]/div/div[2]/div[1]/div[2]/div/label[3]').extract()
        fax = response.xpath('//*[@id="main"]/div/div[2]/div[1]/div[2]/div/label[4]').extract()
        email = response.css('#main .uprofile_dis_wrap_outer .uprofile_dis_wrap span::attr(data-cfemail)').extract()
        
        website = response.xpath('//*[@id="main"]/div/div[2]/div[1]/div[2]/div/label[6]').extract()
        print(email)
        def decodeEmail(email):
            str1 = ''.join(email)
            de = ""
            k = int(str1[:2], 16)

            for i in range(2, len(str1)-1, 2):
                de += chr(int(str1[i:i+2], 16)^k)

            return de
        #speciality = response.css('#main .uprofile_dis_wrap_outer .uprofile_pic_dis').extract()
        #social = response.css('#main .uprofile_social_wrap').extract()

        print ("_______________________________________")

        for item in zip(image,name,company,phone,fax,email,website):
			scraped_info = {
				'image' : item[0],
                'name':item[1],
                'company':item[2],
                'phone':item[3],
                'fax':item[4],
                'email':decodeEmail(item[5]),
                'website':item[6],
			}
			print (scraped_info)
			print ("_______________________________________")

        yield scraped_info

    
    
    
    
    
    #def parse(self, response):
    #    title = response.css('._1vBm_he37k div:nth-of-type(1) p:nth-of-type(1)::text').extract()
    #    description = response.css('._1vBm_he37k div:nth-of-type(1) p:nth-of-type(2)::text').extract()
    #    date = response.css('._1vBm_he37k div:nth-of-type(1) span::text').extract()
        #print ('response',title,description,date)
    #    print ("_______________________________________")

    #    for item in zip(title,description,date):
	#		scraped_info = {
	#			'title' : item[0],
	#			'description' : item[1],
	#			'date' : item[2],
	#		}
            
	#		print (scraped_info)
	#		print ("_______________________________________")

        
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)