from web.models import Screening

from dateutil.parser import parse


class DatabasePipeline(object):

    def process_item(self, item, spider):
        str = item["date"] + " " + item["time"].replace(".", ":")
        datetime = parse(str)
        screening = Screening(title=item["title"],
                              datetime=datetime,
                              age=item["age"])
        import ipdb; ipdb.set_trace()
        screening.save()
        return item
