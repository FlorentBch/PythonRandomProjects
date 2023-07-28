import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
            
# class StuffSpider(scrapy.Spider):
#     name = "Stuff"
#     start_urls = [
#             "https://automatetheboringstuff.com/2e/chapter1/",
#     ]
    
#     def parse(self, response):
#         for title in response.css("h3"):
#             yield {
#                 "sousTitre": title.css("h3 strong::text").get(),
#             }
            
#         next_page = response.css("div center a::attr(href)").get()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        author_page_links = response.css(".author + a")
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css("li.next a")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }