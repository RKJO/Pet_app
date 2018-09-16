# import scrapy
# from WebScrapers.items import AnimalItem
#
#
# class LublinShelterSpider(scrapy.Spider):
#     name = "lublin_shelter"
#
#     def start_requests(self):
#         urls = [
#             'http://www.schronisko-zwierzaki.lublin.pl/index.php?option=com_djcatalog&view=show&cid=1&Itemid=7',
#             # 'http://www.schronisko-zwierzaki.lublin.pl/index.php?option=com_djcatalog&view=show&cid=2&Itemid=17',
#             # 'http://www.schronisko-zwierzaki.lublin.pl/index.php?option=com_djcatalog&view=show&cid=11&Itemid=47',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         item = AnimalItem()
#
#         table_content_rows = response.xpath('//tr[contains(@class, "sectiontableentry")]')
#         for content_row in table_content_rows:
#
#             description_link = content_row.css('.djcat_product a::attr(href)').extract_first()
#
#             item['name'] = content_row.css('.djcat_product a::text').extract_first(),
#             item['species'] = response.css('.componentheading::text').extract_first().split()[0],
#             item['race'] = content_row.css('.djcat_intro span::text').extract_first().split()[-1],
#             item['sex'] = content_row.css('.djcat_intro span::text').extract()[1].split()[-1],
#             item['age'] = content_row.css('.djcat_intro span::text').extract()[2].split()[-1],
#             item['weight'] = content_row.css('.djcat_intro span::text').extract()[3].split()[-1],
#             item['admission_date'] = content_row.css('.djcat_intro span::text').extract()[4].split()[-1],
#             item['sterilized_castrated'] = "",
#             item['evidence_number'] = content_row.css('.djcat_intro span::text').extract()[5].split()[-1],
#
#             # yield response.follow(
#             #     url=description_link,
#             #     callback=self.parse_descryption,
#             #     meta={'item': item}
#             #     )
#
#             yield item
#
#         next_group_pages = response.xpath('//a[contains(@title, "następna")]/@href').extract_first()
#         if next_group_pages is not None:
#             yield response.follow(
#                 url=next_group_pages,
#                 callback=self.parse
#             )
#
#
#     def parse_descryption(self, response):
#         item = response.meta['item']
#
#         item['description'] = " ".join(response.css('.contentpaneopen span::text').extract()),
#         item['img_main'] = response.urljoin(response.css('.dj-catalog-gallery a::attr(href)').extract_first()),
#         item['img_main_alt'] = "",
#         item['img_s'] = "",
#         item['location'] = response.css('#banner span::text').extract_first(),
#         item['url'] = response.url,
#
#         yield item
#
#
#
#
#
#
#
