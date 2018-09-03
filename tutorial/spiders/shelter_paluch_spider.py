import scrapy


class AnimalSpider(scrapy.Spider):
    name = "Animal"
    start_urls = [
        'http://www.napaluchu.waw.pl/czekam_na_ciebie/wszystkie_zwierzeta_do_adopcji/011701269'
    ]

    def parse(self, response):

        # for info in response.css('.info'):

            yield {
                'name': response.css('.info').css('h5::text').extract_first().split(' ')[-5],
                'species': response.css('.info').css('span::text').extract()[0].split(':')[-1].strip(),
                'race': response.css('.info').css('span::text').extract()[1].split(':')[-1].strip(),
                'sex': response.css('.info').css('span::text').extract()[2].split(':')[-1].strip(),
                'age': response.css('.info').css('span::text').extract()[3].split(':')[-1].strip(),
                'weight': response.css('.info').css('span::text').extract()[4].split(' ')[1],
                'admission_date': response.css('.info').css('span::text').extract()[5].split(' ')[-1],
                'evidence_number': response.css('.info').css('span::text').extract()[6].split(' ')[-1],
                'description': ' '.join(' '.join(response.css('.description::text').extract()).split()),
            }


    # response.css('.animals_btn_list_more::attr(href').extract()