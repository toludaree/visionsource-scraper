
from scrapy import Spider
from scrapy.http.response.html import HtmlResponse
from visionsource.items import VisionsourceItem
from itemloaders import ItemLoader


class BusinessesSpider(Spider):
    name = "businesses"
    allowed_domains = ["visionsource.com"]
    start_urls = [
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=10001&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=90001&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=60601&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=77001&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=85001&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=19101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=78201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=92101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=75201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=95101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=73301&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=32099&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=76101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=43085&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=28201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=94101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=46201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=98101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=80201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=20001&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=02101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=79901&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=48201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=37201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=97201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=37501&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=73101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=89101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=40201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=21201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=53201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=87101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=85701&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=93701&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=94203&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=64101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=90801&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=85201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=30301&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=80901&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=23450&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=27601&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=68101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=33101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=94601&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=55401&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=74101&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=67201&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=70112&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=76001&distance=50",
        "https://visionsource.com/patients/find-a-doctor/page1/?zip=44101&distance=50",
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
        pages = response.xpath("//footer[@class='pagination']/p/text()")
        if len(pages) == 0:
            total_pages = 1
        else:
            total_pages = _get_total_pages(pages.get())
        for page in range(2, total_pages+1):
            next_url = f"/page{page}/".join(current_url.split("/page1/"))
            yield response.follow(next_url, callback=self.parse)


def _get_total_pages(text:str) -> int:
    """Given "Page 1 of x", return x"""
    return int(text.split()[-1])
