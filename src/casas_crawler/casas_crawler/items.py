# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from tarfile import FIFOTYPE
import scrapy
from scrapy.item import Item, Field


class CasasCrawlerItem(Item):
    link = Field()
    business_context = Field()
    area = Field()
    bedrooms = Field()
    city = Field()
    bathrooms = Field()
    iptu = Field()
    rent_price = Field()
    condo_price = Field()
    type = Field()
    latitude = Field()
    longitude = Field()
    floor = Field()
    near_subway = Field()
    sale_price = Field()
    construction_year = Field()
    suites = Field()
    state = Field()