from web.models import Screening

from dateutil.parser import parse
import pytz


class DatabasePipeline(object):

    def process_item(self, item, spider):
        parsed = parse(item["date"] + " " + item["time"].replace(".", ":"))
        datetime = pytz.timezone("Europe/London").localize(parsed, is_dst=None)
        screening = Screening(cinema=spider.name,
                              title=item["title"],
                              datetime=datetime,
                              age=item["age"])
        import ipdb; ipdb.set_trace()
        screening.save()
        return item
