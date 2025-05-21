from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

FILE = 'C:/Users/PC/Desktop/Practise/backend/data.json'

FILE = 'C:/Users/PC/Desktop/Practise/backend/data.json'

def load_json():
    with open(FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

        list_key = []
        for entry in data:
            list_key.append(entry['key'])
    return data, list_key



def save_json(data):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
@app.route('/data', methods = ['GET'])
def get_data():
    data, list_key = load_json()
    return jsonify(data), 200

@app.route('/words', methods = ['DELETE'])
def delete_entry():
    data_from_front_end = request.get_json()
    word = data_from_front_end['entry']
    data, _ = load_json()
    data = [item for item in data if item['key'] != word]
    save_json(data)

    return jsonify({'ok': True}), 201

@app.route('/sentences', methods = ['DELETE'])
def delete_sentence():
    data_from_frontend = request.get_json()
    word = data_from_frontend['entry']
    sentence = data_from_frontend['sentence']

    data, _ = load_json()
    for entry in data:
        if entry['key'] == word:
            entry['sentences'] = [s for s in entry['sentences'] if s['sentence'] != sentence]
            break

    save_json(data)

    return jsonify({'ok': True}), 201


@app.route('/backend/audios/<path:filename>')
def server_audios(filename):
    audios_folder = os.path.join(app.root_path, 'audios')
    return send_from_directory(audios_folder, filename)
if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run(port=5000)