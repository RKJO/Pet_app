#!/usr/bin/env bash

cd
# run Vrtualenv
source .virtualenvs/budrys_app_env/bin/activate

cd domains/budrys.org/public_python/

# Run Spiders

scrapy crawl paluch_shelter
scrapy crawl wroclaw_shelter
scrapy crawl czestochowa_shelter
scrapy crawl krakow_shelter

# run Management script

python manage.py delete_adopted
