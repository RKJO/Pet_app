import scrapy


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

    def parse(self, response):
        yield {
            'name': response.css('.info').css('h5::text').extract_first().split(' ')[-5],
            'species': response.css('.info').css('span::text').extract()[0].split(':')[-1].strip(),
            'race': response.css('.info').css('span::text').extract()[1].split(':')[-1].strip(),
            'sex': response.css('.info').css('span::text').extract()[2].split(':')[-1].strip(),
            'age': response.css('.info').css('span::text').extract()[3].split(':')[-1].strip(),
            # todo = use regexp to take only digits of age and weight
            'weight': response.css('.info').css('span::text').extract()[4].split(' ')[1],
            'admission_date': response.css('.info').css('span::text').extract()[5].split(' ')[-1],
            'evidence_number': response.css('.info').css('span::text').extract()[6].split(' ')[-1],
            'description': ' '.join(' '.join(response.css('.description::text').extract()).split()),
            'img_main': response.urljoin(response.css('#main_image_cont a::attr(href)').extract_first()),
            'img_main_alt': response.urljoin(response.css('#main_image_cont img::attr(src)').extract_first()),
            'img_s': [response.urljoin(url) for url in response.css('div.ani_image_bottom a::attr(href)').extract()],
            'location': response.css('#content_slider_left_content_content > div:nth-child(2)::text')\
            .extract_first().split(': ')[-1],
            'url': response.url
        }
