from flask import Flask, jsonify, request, send_from_directory
import json
from flask_cors import CORS
import os
from gtts import gTTS
import re


app = Flask(__name__)
CORS(app)

FILE = 'C:/Users/PC/Desktop/New folder/backend/data.json'

def load_json():
    with open(FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        list_key = []
        for item in data:
            list_key.append(item['key'])
    return data, list_key


def save_json(data):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def safe_filename(sentence):
    # Remove punctuation and replace spaces
    filename = re.sub(r'[^\w\s]', '', sentence)
    filename = filename.replace(' ', '_')
    return filename + '.mp3'

@app.route('/words', methods = ['PUT'])

def update_words():
    data_from_frontend = request.get_json()
    word = data_from_frontend['word'].strip()
    sentence = data_from_frontend['sentence'].strip()

    if not word or not sentence:
        return jsonify({'error': 'sentence is empty'}), 400

    data= load_json()

    for (index, item) in enumerate(data):
        if item['key'] == word:
            audio_filename = safe_filename(sentence)
            audio_path = f'backend/audios/sentences/{audio_filename}'
            item['sentences'].append({
                "sentence" : sentence,
                "audio" : audio_path
            })
            if not os.path.exists(audio_path):
                tts = gTTS(text = sentence, lang='en')
                tts.save(audio_path)


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
    app.run(debug=True, port=5000)


# Invoke-RestMethod -Uri http://localhost:5000/words `
#   -Method PUT `
#   -Body '{"word": "eat", "sentence": "I like to eat apples every morning."}' `
#   -ContentType "application/json"

# http://localhost:5000/backend/audios/sentences/They_ate_all_the_cookies_before_I_arrived.mp3