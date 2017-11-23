import json


class ScreeningEncoder(json.JSONEncoder):

    def default(self, s):
        try:
            to_serialize = {
                'title': s.title,
                'date': s.date,
                'time': s.time,
                'age': s.age
            }
            return to_serialize
        except AttributeError:
            return super(self).default(s)
