from subtitledscreenings.db.db_setup import init_db, db_session
from subtitledscreenings.db.screening import Screening


class DatabasePipeline(object):

    def __init__(self):
        init_db()

    def process_item(self, item, spider):
        screening = Screening(title=item["title"],
                              date=item["date"],
                              time=item["time"],
                              age=item["age"])
        self.add_to_db(screening)
        return item

    def add_to_db(self, screening):
        try:
            db_session.add(screening)
            db_session.commit()
        except:
            db_session.rollback()
            raise Exception("Could not write to db: %s" % screening)
        finally:
            db_session.close()
