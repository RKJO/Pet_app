import scrapy
import datetime

from WebScrapers.items import AnimalItem
from WebScrapers.parsers import parse_location, animal_update_or_create, parse_size


class PaluchShelterSpider(scrapy.Spider):
    name = "paluch_shelter"

    def start_requests(self):
        urls = [
            'http://www.napaluchu.waw.pl/czekam_na_ciebie/wszystkie_zwierzeta_do_adopcji:1'
        ]
        yield scrapy.Request(url=urls[0], callback=self.next_page)

    def next_page(self, response):
        next_group_pages = response.css('a.next::attr(href)').extract_first()
        pages = response.css('.animals_btn_list_more::attr(href)').extract()
        for page in pages:
            if page is not None:
                page = response.urljoin(page)
                yield scrapy.Request(page, callback=self.parse)
        if next_group_pages is not None:
            yield response.follow(next_group_pages, callback=self.next_page)

    def parse_administration_date(self, date_str):
        date = date_str.split(".")
        date_time = datetime.datetime(year=int(date[-1]), month=int(date[1]), day=int(date[0]))
        return date_time.strftime('%Y-%m-%d')

    def parse(self, response):
        item = AnimalItem()

        item['name'] = response.css('.info').css('h5::text').extract_first().split(' ')[-5]
        item['species'] = (response.css('.info').css('span::text').extract()[0].split(':')[-1].strip()).lower()
        item['race'] = response.css('.info').css('span::text').extract()[1].split(':')[-1].strip()
        item['sex'] = (response.css('.info').css('span::text').extract()[2].split(':')[-1].strip()).lower()
        item['age'] = response.css('.info').css('span::text').extract()[3].split(' ')[-2]
        item['weight'] = int(response.css('.info').css('span::text').extract()[4].split(' ')[1])
        item['size'] = parse_size(item.get('weight'), item.get('species'))
        item['admission_date'] = self.parse_administration_date(response.css('.info').css('span::text').extract()[5].split(' ')[-1])
        item['evidence_number'] = response.css('.info').css('span::text').extract()[6].split(' ')[-1]
        item['description'] = ' '.join(' '.join(response.css('.description::text').extract()).split())
        item['img_main'] = response.urljoin(response.css('#main_image_cont a::attr(href)').extract_first())
        item['img_main_alt'] = response.urljoin(response.css('#main_image_cont img::attr(src)').extract_first())
        item['img_s'] = [response.urljoin(url) for url in response.css('div.ani_image_bottom a::attr(href)').extract()[0:3]]
        item['location'] = parse_location(response.css('#content_slider_left_content_content > div:nth-child(2)::text').extract_first().split(': ')[-1])
        item['url'] = response.url

        animal_update_or_create(item)
