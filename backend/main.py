from flask import Flask, jsonify, request, send_from_directory
import json
from flask_cors import CORS
import os
from gtts import gTTS
import os
import re


app = Flask(__name__)
CORS(app)
FILE_1 = 'C:/Users/PC/Desktop/New folder/backend/data.json'
FILE_2 = 'C:/Users/PC/Desktop/New folder/backend/self.json'

def load_json(FILE):
    with open(FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_json(data):
    with open(FILE_1, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def safe_filename(sentence):
    # Keep only alphanumeric characters and spaces
    filename = re.sub(r'[^\w\s]', '', sentence)
    filename = filename.replace(' ', '_')
    return filename + '.mp3'


@app.route('/words', methods = ['POST'])
def add_words():
    data_from_frontend = request.get_json()
    word = data_from_frontend['word']
    data = load_json(FILE_1)

    exist = False
    for item in data:
        if item['key'] == word:
            item['number'] += 1
            exist = True
            break
    if not exist:
        data.append(
            {
                "key": word,
                "number": 4,
                "audio": f"backend/audios/words/{word}.mp3",
                "sentences": []
            }
        )

        if not os.path.exists(f"backend/audios/words/{word}.mp3"):
            tts = gTTS(text = word, lang='en')
            tts.save(f"backend/audios/words/{word}.mp3")

    save_json(data)
    return jsonify({'ok': True}), 201

@app.route('/words', methods = ['PUT'])

def update_words():
    data_from_frontend = request.get_json()
    word = data_from_frontend['word'].strip()
    sentence = data_from_frontend['sentence'].strip()

    if not word or not sentence:
        return jsonify({'error': 'sentence is empty'}), 400

    data = load_json(FILE_1)

    for (index, item) in enumerate(data):
        if item['key'] == word:
            audio_filename = safe_filename(sentence)
            audio_path = f'backend/audios/sentences/{audio_filename}'
            item['sentences'].append({
                "sentence" : sentence,
                "audio" : audio_path
            })
            print(item['sentences'])
            if not os.path.exists(audio_path):
                tts = gTTS(text = sentence, lang='en')
                tts.save(audio_path)

            item['number'] -= 1
            print(item['number'])
            save_json(data)
            break


    return jsonify({'ok': True}), 201


@app.route('/words', methods = ['GET'])
def get_data():
    data = load_json(FILE_1)
    return jsonify(data), 200


@app.route('/self', methods = ['GET'])
def get_self():
    data = load_json(FILE_2)
    return jsonify(data), 201



@app.route('/words', methods = ["Delete"])
def delete_word():
    data_from_frontend = request.get_json()
    word = data_from_frontend['word']
    data = load_json(FILE_1) 
    for item in data:
        if item['key'] == word:
            if os.path.exists(item['audio']):
                os.remove(item['audio'])
             
            for data_sentence in item['sentences']:
                if os.path.exists(data_sentence['audio']):
                    os.remove(data_sentence['audio'])

    data = [item for item in data if item['key'] != word]
    save_json(data)
    return jsonify({'ok': True}), 200


@app.route('/backend/audios/<path:filename>')
def server_audios(filename):
    audios_folder = os.path.join(app.root_path, 'audios')
    return send_from_directory(audios_folder, filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
