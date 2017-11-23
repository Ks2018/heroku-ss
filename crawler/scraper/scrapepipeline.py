from scrapy.exceptions import DropItem
import re


class ScrapePipeline(object):

    running_date = ""
    hoh = "HOH Subtitled"

    def process_item(self, item, spider):
        if item["date"]:
            self.running_date = item["date"][0]
        if self.hoh in item["time"]:
            item = self.consolidate_fields(item)
            return item
        else:
            raise DropItem("Not subtitled %s" % item)

    def consolidate_fields(self, item):
        hoh_index = item["time"].index(self.hoh)
        item["time"] = item["time"][hoh_index - 1]
        item["date"] = self.running_date
        item["age"] = self.extract_age(item["title"][0])
        item["title"] = item["title"][0].replace(' [' + item["age"] + ']', "")
        return item

    def extract_age(self, title):
        return re.search(r"\[(\w+)\]", title).group(1)
