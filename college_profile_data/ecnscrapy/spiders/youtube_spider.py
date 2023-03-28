import scrapy
import os, sys
import csv
#import mysql.connector
#from mysql.connector import Error

class YoutubeSpider(scrapy.Spider):
	name = 'youtube'
	allowed_domains = ['https://www.youtube.com']
	
	currentPath = os.path.dirname(__file__)
	#path for the filename that we want to read
	filePath = os.path.abspath(os.path.join(currentPath, os.pardir,os.pardir,'data'))
	#print(filePath)
	your_list = list()
	with open('YoutubeUrls.csv', 'r') as f:
		reader = csv.reader(f)
		for line_list in reader:
			your_list.append(line_list[0])
	print(your_list)
	#start_urls = ['https://www.globalgolf.com/golf-clubs/1033036-titleist-816-h1-hybrid/used/', 'https://www.globalgolf.com/golf-clubs/1037608-taylormade-m2-2017-fairway-wood/', 'https://www.globalgolf.com/golf-clubs/1037604-taylormade-m2-2017-driver/', 'https://www.globalgolf.com/golf-clubs/1036431-titleist-917d2-driver/', 'https://www.globalgolf.com/golf-clubs/1036436-titleist-917f2-fairway-wood/', 'https://www.globalgolf.com/golf-clubs/1037615-taylormade-m2-rescue-2017-hybrid/', 'https://www.globalgolf.com/golf-clubs/1034510-titleist-vokey-sm6-tour-chrome-f-grind-wedge/', 'https://www.globalgolf.com/golf-clubs/1033029-titleist-ap1-716-iron-set/', 'https://www.globalgolf.com/golf-clubs/1034418-taylormade-m2-fairway-wood/used/', 'https://www.globalgolf.com/golf-clubs/1037598-taylormade-m1-2017-fairway-wood/']
	start_urls = your_list

	def parse(self, response):
		#conn = mysql.connector.connect(host='localhost',database='scrapy',user='root',password='')
		#if conn.is_connected():
		#	print('Connected to MySQL database')
		#cursor = conn.cursor(dictionary=True)
		#query = "INSERT INTO golf(title,price,avgrating,ratings,description,description2) VALUES(%s,%s,%s,%s,%s,%s)"
		titles = response.css('[id="prodTitle"]::text').extract()
		prices = response.css('[id="lblProductPrice"]::text').extract()
		avgrating = response.css('.ratingbar div:nth-of-type(1)::attr(style)').extract()
		ratings = response.css('.revNum a:nth-of-type(1)::text').extract()
		description = response.css('.desc div:nth-of-type(2)::text').extract()
		description2 = response.css('.desc div:nth-of-type(3)::text').extract()


		for item in zip(titles,prices,avgrating,ratings,description,description2):
			scraped_info = {
				'title' : item[0],
				'price' : item[1],
				'avgrating' : item[2],
				'ratings' : item[3],
				'description' : item[4],
				'description2' : item[5]
			}
			
			avgratingfinal = scraped_info['avgrating'].replace("width:","")
			ratingsfinal = scraped_info['ratings'].replace(" reviews)","")
			args = (scraped_info['title'], scraped_info['price'], avgratingfinal.replace(";",""), ratingsfinal.replace("(",""), scraped_info['description'], scraped_info['description2'])
			#cursor.execute(query, args)
			#if cursor.lastrowid:
			#	print('last insert id', cursor.lastrowid)
			#else:
			#	print('last insert id not found')

			print (scraped_info['title'])
			print (scraped_info['price'])
			print (avgratingfinal.replace(";",""))
			print (ratingsfinal.replace("(",""))
			print (scraped_info['description'])
			print (scraped_info['description2'])
			print ("_______________________________________")

		#conn.close()
 
if __name__ == '__main__':
		connect()
