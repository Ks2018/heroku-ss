import json

from flask import Flask, jsonify, make_response

from subtitledscreenings.db.db_setup import db_session
from subtitledscreenings.db.screening import Screening
from subtitledscreenings.utils.serializer import ScreeningEncoder

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Subtitled Screenings!'


@app.route('/api/screenings/<int:id>', methods=['GET'])
def get_screening(id):
    screening = Screening.query.filter(Screening.id == id).first()
    if screening:
        serialized = (json.dumps(screening, cls=ScreeningEncoder))
        return jsonify(serialized)
    else:
        return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/screenings', methods=['GET'])
def get_screenings():
    screenings = Screening.query.all()
    serialized = (json.dumps(screenings, cls=ScreeningEncoder))
    return jsonify({'screenings': serialized})


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
