# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook
from openpyxl.styles import Font


class VisionsourceDoctorsDefaultValuePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        if not adapter.get("doctors"):
            adapter["doctors"] = []
            return item
        else:
            return item
    
class VisionsourcePhoneNumberDefaultValuePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if not adapter.get("phone_number"):
            adapter["phone_number"] = ""
            return item
        else:
            return item
    
class VisionsourceWebsiteDefaultValuePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if not adapter.get("website"):
            adapter["website"] = ""
            return item
        else:
            return item
        
        
class VisionsourceAddToXlsxPipeline:
    def __init__(self):
        self.workbook = None
        self.worksheet = None
        self.current_row_index = 0

    def process_item(self, item, spider):
        item["doctors"] = ", ".join(item["doctors"])
        values = list(item.values())

        # add header at first row
        if self.current_row_index == 0:
            # get header from item keys
            header = list(item.keys())
            self.worksheet.append(header)
            bold_font = Font(bold=True)
            for cell in self.worksheet[1]:
                cell.font = bold_font
            # After add header, add value below the header
            self.worksheet.append(values)
        else:
            self.worksheet.append(values)

        self.current_row_index += 1

        return item
    
    def open_spider(self, spider):
        self.workbook = Workbook()
        self.worksheet = self.workbook.active

    def close_spider(self, spider):
        excel_file = "houses.xlsx"
        self.workbook.save(excel_file)
