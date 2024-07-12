# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import Join, MapCompose


def doctors_in(d:str):
    return d.split(",")

def doctors_out(d:str):
    return d.strip()

def address_out(d:list[str]):
    return "; ".join(d)

def phone_number_in(d):
    return d.strip()


class VisionsourceItem(Item):
    business_name = Field(output_processor=Join())
    doctors = Field(input_processor=MapCompose(doctors_in),
                    output_processor=MapCompose(doctors_out))
    address = Field(output_processor=address_out)
    phone_number = Field(input_processor=MapCompose(phone_number_in),
                         output_processor=Join())
    website = Field(output_processor=Join())
