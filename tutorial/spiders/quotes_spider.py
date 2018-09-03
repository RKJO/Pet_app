import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#         'http://quotes.toscrape.com/page/2/',
#     ]
#
#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'http://quotes.toscrape.com/page/1/',
#         'http://quotes.toscrape.com/page/2/',
#     ]
#
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.css('small.author::text').extract_first(),
#                 'tags': quote.css('div.tags a.tag::text').extract(),
#             }


class DogsSpider(scrapy.Spider):
    name = "dogs"
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


        # yield {
        #     'name': dog_info.css('h5::text').extract_first().split(' ')[-5],
        #     'species': dog_info.css('span::text').extract()[0].split(':')[-1].strip(),
        #     'race': dog_info.css('span::text').extract()[1].split(':')[-1].strip(),
        #     'sex': dog_info.css('span::text').extract()[2].split(':')[-1].strip(),
        #     'age': dog_info.css('span::text').extract()[3].split(':')[-1].strip(),
        #     'weight': dog_info.css('span::text').extract()[4].split(' ')[1],
        #     'admission_date': dog_info.css('span::text').extract()[5].split(' ')[-1],
        #     'evidence_number': dog_info.css('span::text').extract()[6].split(' ')[-1],
        # }