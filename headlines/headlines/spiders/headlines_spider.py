import scrapy

class HeadlineSpider(scrapy.Spider):
    name = 'headline'
    start_url = [
        'https://www.nytimes.com/spotlight/learning-stem'
    ]

    def parse(self, response):
        headline = response.css('.e15t083i0::text').extract()
        yield {'headlineText': headline}

