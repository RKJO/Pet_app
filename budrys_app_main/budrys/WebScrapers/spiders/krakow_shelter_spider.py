import scrapy

from WebScrapers.parsers import parse_location


class KrakowShelterSpider(scrapy.Spider):
    name = "krakow_shelter"

    def start_requests(self):
        urls = [
            'http://www.schronisko.krakow.pl/Adopcje/ZWIERZAKI_DO_ADOPCJI/Psy/',
            'http://www.schronisko.krakow.pl/Adopcje/ZWIERZAKI_DO_ADOPCJI/Koty/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.next_page)

    def next_page(self, response):
        next_group_pages = response.css('a.right_double_arrow::attr(href)').extract_first()
        pages = response.css('.news_short_more::attr(href)').extract()
        for page in pages:
            if page is not None:
                page = response.urljoin(page)
                yield scrapy.Request(page, callback=self.parse)
        if next_group_pages is not None:
            yield response.follow(next_group_pages, callback=self.next_page)

    def parse(self, response):
        metrics_element = response.css('.default_description').css('b::text').extract()
        description_element = response.css('.default_description').css('p::text').extract()
        yield {
            'name': metrics_element[0],
            'species': metrics_element[3].split(':')[-1].strip(),
            'race': metrics_element[4].split(':')[-1].strip(),
            'sex': "",
            'age': "",
            'weight': metrics_element[-1].split(':')[-1].strip()
            'admission_date': metrics_element[2].split(':')[-1].strip(),
            'evidence_number': metrics_element[1].split(':')[-1].strip(),
            'description': ' '.join(' '.join(description_element[-3:]).split()),
            'img_main': response.urljoin(response.css('.animal_big_foto img::attr(src)').extract_first()),
            # 'img_main_alt': response.urljoin(response.css('.photo_gallery_str a::attr(href)').extract()[1]),
            'img_s': [response.urljoin(url) for url in response.css('.photo_gallery_str a::attr(href)').extract()[1:]],
            'location': parse_location(' '.join(response.selector.xpath('//*[@id="footer_right"]/div/text()').extract()[1].split())),
            'url': response.url
        }
