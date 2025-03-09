from flask import *
from flask_cors import CORS
import updater
from get_data import get_data, file_exists, save_data

app = Flask(__name__)
CORS(app)

@app.route('/weather')
def weather_data():
    req = get_data()
    print(req)
    return req

@app.route('/get_preset_city', methods=['GET'])
def get_preset_city():
    res = request.args.get('city')
    print(res)
    if(file_exists(res)):
        return get_data(res)
    else:
        "adding requested city"
        return get_data(res)
    
@app.route('/save_theme', methods=['POST'])
def save_theme():
    res = request.json["theme"]
    print(res)
    return save_data(res, 'theme')

@app.route('/get_theme', methods=['GET'])
def get_theme():
    res = get_data('theme')
    return res

def main():
    updater.update_data()
    app.run(port=5048)