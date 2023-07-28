from scrapy import Request, Spider
from ..items import ReviewAllocineItem


class SpiderReviewsAllocine(Spider):
    # Nom du Spider
    name = "Reviews_allocine"
    # URL de la page à scraper
    url = "https://www.allocine.fr/film/fichefilm-10568/critiques/spectateurs/"
    index = 1
    start_URL = "https://www.allocine.fr/film/fichefilm-10568/critiques/spectateurs/"
    def start_requests(self):
        yield Request(url=self.url, callback=self.parse_films)

    def parse_films(self, response):
        title = response.css("a.titlebar-link::text").extract_first()
        review_blocks = response.css("div.review-card")
        for review_card in review_blocks:
            self.index += 1
            review = review_card.css("div.content-txt::text").extract_first()
            stars = review_card.css("span.stareval-note::text").extract_first()
            # Pour avoir la note (nombre d'étoiles) en float
            stars = float(stars.replace(",", "."))

            item = ReviewAllocineItem()

            item['title'] = title
            item['stars'] = stars
            item['review'] = review

            yield item
            
        # NextPage = 'https://www.allocine.fr/film/fichefilm-10568/critiques/spectateurs/?page'+ self.index
        # if self.index <=10:
        #     yield response.follow(NextPage, callback = self.parse)
            
            # next_page = response.css('a.next::attr(href)').get()
            # if next_page is not None:
            #     yield response.follow(next_page, self.parse)
