import scrapy


class QuoterSpider(scrapy.Spider):
    name = "quoter"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/page/1/",
                 "http://quotes.toscrape.com/page/1/ ",
                 ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "auth": quote.css("span small::text").get(),
                "tag": quote.css("div.tags a.tag::text").getall(),
            }
        nextpage = response.css("li.next a::attr(href)").get()
        if nextpage is not None:
            yield response.follow(nextpage,callback=self.parse)