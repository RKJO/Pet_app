import scrapy

from WebScrapers.items import AnimalItem
from WebScrapers.parsers import parse_location, animal_update_or_create


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
        item = AnimalItem()
        metrics_element = response.css('.table-profile-description td:nth-child(2) > strong::text').extract()

        item['name'] = response.css('.h-serif-flex::text').extract_first().strip()
        item['species'] = (metrics_element[-1].split()[0]).lower()
        # item['race'] = ""
        # item['sex'] = ""
        # item['age'] = ""
        # item['weight'] = ""
        item['admission_date'] = metrics_element[1]
        item['sterilized_castrated'] = ""
        item['evidence_number'] = metrics_element[0].strip()
        item['description'] = response.css('.profile-description-sub-content::text').extract()[1].split("\n")[0].strip()
        item['img_main'] = response.urljoin(response.css('.gallery-group a::attr(href)').extract_first())
        item['img_main_alt'] = response.urljoin(response.css('.photo_gallery_str a::attr(href)').extract()[1:])
        # item['img_s'] = ""
        item['location'] = parse_location((' '.join([location.strip() for location in response.css('.par-contact-left::text').extract()[1:3]])).split('. ')[1])
        item['url'] = response.url

        animal_update_or_create(item)
        # yield item