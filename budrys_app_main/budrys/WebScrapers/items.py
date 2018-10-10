# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from budrys_app.models import Animals


class AnimalItem(DjangoItem):
    djangoer_model = Animals

# class AnimalItem(scrapy.Item):
#     name = scrapy.Field()
#     species = scrapy.Field()
#     race = scrapy.Field()
#     sex = scrapy.Field()
#     age = scrapy.Field()
#     weight = scrapy.Field()
#     admission_date = scrapy.Field()
#     sterilized_castrated = scrapy.Field()
#     evidence_number = scrapy.Field()
#     description = scrapy.Field()
#     img_main = scrapy.Field()
#     img_main_alt = scrapy.Field()
#     img_s = scrapy.Field()
#     url = scrapy.Field()


