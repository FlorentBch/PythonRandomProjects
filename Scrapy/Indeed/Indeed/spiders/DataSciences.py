from scrapy import Request, Spider
from ..items import IndeedScrap

class IndeedSpider(Spider):
    name = 'indeed'
    allowed_domains = ['indeed.com']
    url = "https://www.indeed.fr/jobs?q=data+scientist&l=Paris%2C+France"


    def start_requests(self):
        yield Request(url=self.url, callback=self.parse)
    
    def parse(self, response):
        # Extraire les offres d'emploi de la page actuelle
        title = response.xpath('//*[@id="UploadYourResume"]').extract_first()
        for job in response.css('div.cardOutline'):
            
            title = job.css('a.jcs-JobTitle::text').extract_first()
            # 'company': job.css('span.companyName::text').get()
            # 'location': job.css('div.companyLocation::text)').get()
            
            item = IndeedScrap()
            
            item['title'] = title
            
            yield item

        # Suivre le lien vers la page suivante
        # next_page = response.css('a[aria-label="Next"]::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
