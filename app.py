from flask import Flask
from datastorage import Town, session

app = Flask(__name__)

@app.route("/api/bounds/<left>/<top>/<right>/<bottom>/")
def get_places_by_bounds(left, top, right, bottom):
    towns = session.query(Town).filter(Town.latitude >= left,
                                       Town.latitude <= right,
                                       Town.longitude >= top,
                                       Town.longitude <= bottom)

    return json.dumps([town.to_dict() for town in towns])
