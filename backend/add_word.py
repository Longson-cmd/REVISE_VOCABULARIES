from flask import Flask, request, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


FILE = 'C:/Users/PC/Desktop/Practise/backend/data.json'

def load_data():
    with open(FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

        list_key = []
        for entry in data:
            list_key.append(entry['key'])
    return data, list_key

def save_data(data):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/words', methods = ['POST'])



def add_entry():
    data_from_frontend = request.get_json()
    word = (data_from_frontend['word'] or '').strip()

    if not word:
        return jsonify({'error': 'Sentence is empty'}), 400
    
    data, list_key = load_data()

    if word in list_key:
        for index, entry in enumerate(data):
            if entry['key'] == word:
                data[index]['number'] +=1 
                save_data(data)
                return jsonify({'ok': True, 'total': len(data)}), 201
    else:
        entry = {}
        entry['key'] = word
        entry['number'] = 5
        entry['audio'] = f'backend/audios/words/{word}.wav'
        entry['sentences'] = []
        data.append(entry)

        save_data(data)
        return jsonify({'ok': True, 'total': len(data)}), 201


if __name__ == '__main__':
    app.run(port = 5000)
