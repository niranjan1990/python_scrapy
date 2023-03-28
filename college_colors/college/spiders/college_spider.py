import scrapy


class ColorsSpider(scrapy.Spider):
    name = "colors"

    def start_requests(self):
        urls = [
            'https://teamcolorcodes.com/ncaa-color-codes/america-east/',
            'https://teamcolorcodes.com/ncaa-color-codes/aac/',
            'https://teamcolorcodes.com/ncaa-color-codes/acc-color-codes/',
            'https://teamcolorcodes.com/ncaa-color-codes/atlantic-sun/',
            'https://teamcolorcodes.com/ncaa-color-codes/atlantic-10-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/big-east/',
            'https://teamcolorcodes.com/ncaa-color-codes/big-sky-conference/',
            'https://teamcolorcodes.com/ncaa-color-codes/big-south-conference-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/big-west/',
            'https://teamcolorcodes.com/ncaa-color-codes/big-ten-team-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/big-12-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/colonial-athletic-association-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/conference-usa/',
            'https://teamcolorcodes.com/ncaa-color-codes/horizon-league/',
            'https://teamcolorcodes.com/ncaa-color-codes/ivy-league/',
            'https://teamcolorcodes.com/ncaa-color-codes/maac/',
            'https://teamcolorcodes.com/ncaa-color-codes/mac/',
            'https://teamcolorcodes.com/ncaa-color-codes/mid-eastern-athletic-conference-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/missouri-valley/',
            'https://teamcolorcodes.com/ncaa-color-codes/mountain-west/',
            'https://teamcolorcodes.com/ncaa-color-codes/northeast-conference-nec-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/ohio-valley-conference-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/pac-12-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/patriot-league-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/sec-team-color-codes/',
            'https://teamcolorcodes.com/ncaa-color-codes/southern-conference-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/southland-conference-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/summit-league/',
            'https://teamcolorcodes.com/ncaa-color-codes/sun-belt/',
            'https://teamcolorcodes.com/ncaa-color-codes/southwestern-athletic-conference-colors/',
            'https://teamcolorcodes.com/ncaa-color-codes/western-athletic-conference/',
            'https://teamcolorcodes.com/ncaa-color-codes/west-coast-conference/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('response',response)
        for a in response.css("#genesis-content > article > div"):
            college = a.css("a::text").extract()
            style = a.css("a::attr(style)").extract()
            #print('collegestyle',college,style)
            page =[]
            for item in zip(college,style):
                scraped_info = {
                    'college' : item[0],
                    'style' : item[1],
                }
                print('scrapedinfo',scraped_info)
                page.append(scraped_info)
            print('page',page)
            return(page)
            

