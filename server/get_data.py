import requests
import json
import os

city="Lusaka"
res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3b7d95ef4a86b41f16d97906434e5180&units=metric')


def get_data(db_file=city):
    if file_exists(db_file):
        with open(f"weather_{db_file}.json", 'r') as file:
            data = json.load(file)
            return data
    else:
        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={db_file}&appid=3b7d95ef4a86b41f16d97906434e5180&units=metric')
        return data.json()

def file_exists(name):
    if os.path.exists(f"weather_{name}.json"):
        return True
    else:
        return False


def save_data(data, data_storage):
    del_res = delete_data(data_storage)
    try:
        with open(f"weather_{data_storage}.json", "w") as file:
            json.dump(data.json(), file, indent=4)
        return "done"
    except:
        try:
            with open(f"weather_{data_storage}.json", "w") as file:
                json.dump(data, file, indent=4)
            return "done"
        except:
            return "Failed"

def delete_data(file):
    if os.path.exists(f"weather_{file}.json"):
        os.remove(f"weather_{file}.json")
        return "deleted succesfully"
    
    else:
        return "No file with that name was found..."
    
def update():
    save_data(res, city)
