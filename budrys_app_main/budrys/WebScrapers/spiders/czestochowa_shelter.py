import scrapy


class CzestochowaShelterSpider(scrapy.Spider):
    name = "czestochowa_shelter"

    def start_requests(self):
        urls = [
            'http://www.schronisko.czestochowa.pl/animals.php?GroupId=1',
            'http://www.schronisko.czestochowa.pl/animals.php?GroupId=2',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.next_page)

    def next_page(self, response):
        next_group_pages = response.css('#list-navigation  a::attr(href)').extract()[-1]
        pages = response.css('.animal-read-more a::attr(href)').extract()
        for page in pages:
            if page is not None:
                yield response.follow(page, callback=self.parse)
        if next_group_pages is not None:
            yield response.follow(next_group_pages, callback=self.next_page)

    def parse(self, response):
        metrics_element = response.xpath('//*[@id="main-top-one-info"]/p[1]/text()').extract()
        gallery = response.css('.gallery a::attr(href)')
        yield {
            'name': metrics_element[1].strip(),
            'species': metrics_element[3].strip(),
            'race': metrics_element[7].strip(),
            'sex': "",
            'age': metrics_element[5].strip(),
            'weight': metrics_element[11].strip(),
            'admission_date': "",
            'sterilized/castrated': metrics_element[13].strip(),
            'evidence_number': metrics_element[15].strip(),
            'description': ' '.join(metrics_element[19].split()),
            'img_main': response.urljoin(gallery.extract_first()),
            # 'img_main_alt': response.urljoin(response.css('.photo_gallery_str a::attr(href)').extract()[1]),
            'img_s': [response.urljoin(url) for url in gallery.extract()[1:]],
            'location': response.xpath('//*[@id="main-top-one-info"]/p[2]/text()').extract()[1].split("\n")[1],
            'url': response.url,
        }
