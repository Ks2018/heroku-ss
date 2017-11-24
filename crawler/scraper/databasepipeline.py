from web.models import Screening


class DatabasePipeline(object):

    def process_item(self, item, spider):
        screening = Screening(title=item["title"],
                              date=item["date"],
                              time=item["time"],
                              age=item["age"])
        screening.save()
        return item
