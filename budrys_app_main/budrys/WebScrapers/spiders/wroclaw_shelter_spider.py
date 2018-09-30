import scrapy

from WebScrapers.parsers import parse_location


class WroclawShelterSpider(scrapy.Spider):
    name = "wroclaw_shelter"

    def start_requests(self):
        urls = [
            'https://www.schroniskowroclaw.pl/adopcja/psy-do-adopcji-c2',
            'https://www.schroniskowroclaw.pl/adopcja/koty-c9',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.next_page)

    def next_page(self, response):
        next_group_pages = response.css('.pagination  a::attr(href)').extract()[-1]
        pages = response.css('a.thumbnail::attr(href)').extract()
        for page in pages:
            if page is not None:
                yield response.follow(page, callback=self.parse)
        if next_group_pages is not None:
            yield response.follow(next_group_pages, callback=self.next_page)

    def parse(self, response):
        metrics_element = response.css('.table-profile-description td:nth-child(2) > strong::text').extract()
        yield {
            'name': response.css('.h-serif-flex::text').extract_first().strip(),
            'species': metrics_element[-1].split()[0],
            'race': "",
            'sex': "",
            'age': "",
            'weight': "",
            'admission_date': metrics_element[1],
            'sterilized/castrated': "",
            'evidence_number': metrics_element[0].strip(),
            'description': response.css('.profile-description-sub-content::text').extract()[1].split("\n")[0].strip(),
            'img_main': response.urljoin(response.css('.gallery-group a::attr(href)').extract_first()),
            # 'img_main_alt': response.urljoin(response.css('.photo_gallery_str a::attr(href)').extract()[1]),
            'img_s': "",
            'location': parse_location(' '.join([location.strip() for location in response.css('.par-contact-left::text').extract()[1:3]])),
            'url': response.url,
        }
