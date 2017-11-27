import re

import pytz
from dateutil.parser import parse
from scrapy.exceptions import DropItem


class ParsePipeline(object):

    running_date = ""
    hoh = "HOH Subtitled"

    def process_item(self, item, spider):
        if item["date"]:
            self.running_date = item["date"][0]
        if self.hoh in item["time"]:
            item = self._consolidate_fields(item, spider)
            return item
        else:
            raise DropItem("Not subtitled %s" % item)

    def _consolidate_fields(self, item, spider):
        hoh_index = item["time"].index(self.hoh)
        item["cinema"] = spider.name
        item["time"] = item["time"][hoh_index - 1]
        item["date"] = self.running_date
        item["age"] = self._extract_age(item["title"][0])
        item["title"] = item["title"][0].replace(' [' + item["age"] + ']', "")
        item["datetime"] = self._parse_datetime(item)
        return item

    def _parse_datetime(self, item):
        parsed = parse(item["date"] + " " + item["time"].replace(".", ":"))
        datetime = pytz.timezone("Europe/London").localize(parsed, is_dst=None)
        return datetime

    def _extract_age(self, title):
        return re.search(r"\[(\w+)\]", title).group(1)
