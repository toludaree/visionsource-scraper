
from scrapy import Spider
from visionsource.items import VisionsourceItem
from itemloaders import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BusinessesSpider(Spider):
    name = "businesses"
    allowed_domains = ["visionsource.com"]
    start_urls = [
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=10001&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=90001&distance=50",
    ]

    def parse(self, response):
        gallery = response.xpath("//div[@class='list-item']")
        for business in gallery:
            item = ItemLoader(item=VisionsourceItem(),
                              response=response,
                              selector=business)

            item.add_xpath("business_name", "./h2/text()")
            item.add_xpath("doctors", "./p[@class='doctors']/text()")
            item.add_xpath("address", "./div[@class='address']/p/text()")
            item.add_xpath("phone_number", "./div[@class='contact']/p/text()")
            item.add_xpath("website", "./div[@class='action']/a[contains(text(), 'Visit Website')]/@href")

            yield item.load_item()
