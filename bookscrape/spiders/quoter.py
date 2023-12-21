import scrapy


class QuoterSpider(scrapy.Spider):
    name = "quoter"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/page/1/",
                 "http://quotes.toscrape.com/page/1/ ",
                 ]

    def parse(self, response):
        quotes = response.css(".quote .text::text").getall()

        yield {
            "text":quotes
        }
