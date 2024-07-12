# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import Join


class VisionsourceItem(Item):
    business_name = Field(output_processor=Join())
    doctors = Field(output_processor=Join())
    address = Field(output_processor=Join())
    phone_number = Field(output_processor=Join())
    website = Field(output_processor=Join())
