from scrapy import Request, Spider
from ..items import ListeDesAliments

class SpiderListe(Spider):
    
    name = "Liste"
    url = "https://listonic.com/fr/liste-de-courses-basiques/"
    
    def start_requests(self):
        yield Request(url=self.url, callback=self.parse)
        
    def parse(self, response):
        title = response.css("h1.article-title::text").extract_first()
        review_blocks = response.css("div.right")
        
        for items in review_blocks:
            nourriture = items.xpath('//*[@id="menu-item-14754"]/a/text()').extract_first()
            item = ListeDesAliments()
            item['nourriture'] = nourriture
            item['titre'] = title
            
            yield item