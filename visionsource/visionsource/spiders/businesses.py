
from scrapy import Spider
from scrapy.http.response.html import HtmlResponse
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

    def parse(self, response:HtmlResponse):
        gallery = response.xpath("//div[@class='list-item']")
        for business in gallery:
            item = ItemLoader(item=VisionsourceItem(),
                              response=response,
                              selector=business)

            item.add_xpath("business_name", "./h2/text()")
            item.add_xpath("doctors", "./p[@class='doctors']/text()")
            item.add_xpath("address", "./div[@class='address']/p/text()")
            item.add_xpath("phone_number", "./div[@class='contact']/p/text()")
            item.add_xpath("website",
                           "./div[@class='action']" \
                           "/a[contains(text(), 'Visit Website')]/@href")

            yield item.load_item()

        current_url = response.url
        total_pages = _get_total_pages(
            response.xpath("//footer[@class='pagination']/p/text()").get()
        )
        for page in range(2, total_pages+1):
            next_url = f"/page{page}/".join(current_url.split("/page1/"))
            yield response.follow(next_url, callback=self.parse)


def _get_total_pages(text:str) -> int:
    """Given "Page 1 of x", return x"""
    return int(text.split()[-1])
