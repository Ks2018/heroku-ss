from web.models import Screening


class DatabasePipeline(object):

    def process_item(self, item, spider):
        screening = Screening(cinema=item["cinema"],
                              title=item["title"],
                              datetime=item["datetime"],
                              age=item["age"])
        screening.save()
        return item
