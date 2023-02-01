import scrapy

class GisSpider(scrapy.Spider):

    name = 'gis'
    custom_settings = {

        'FEEDS': {'data.csv': {'format': 'csv'}}
    }
    def start_requests(self):
        
        urls = []

        for i in range(1,3):
            urls.append(f'https://search.open.canada.ca/opendata/?page={i}&sort=date_modified+desc&subject_en=Nature+and+Environment')
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        maincontent = response.xpath('//main')
        selectors = maincontent[0].xpath('//div[@class="row mrgn-bttm-xl mrgn-lft-md"]')

        for node in selectors:
            rows = node.xpath('div[@class="row"]')
            title = rows[0].xpath('.//strong/text()').extract()
            mytitle = title[0].strip()

            dates = rows[2].xpath('.//div[@class="col-sm-6"]/text()').extract()
            updated = ''.join(dates[:2]).strip()
            published = ''.join(dates[2:]).strip()

            yield {'title': mytitle, 'updated': updated, 'published': published}

