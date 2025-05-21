from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from gtts import gTTS


app = Flask(__name__)
CORS(app)


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


@app.route('/words', methods = ['PUT'])


def add_sentence():
    data_from_frontend = request.get_json()
    word = data_from_frontend['key']
    sentence_text = data_from_frontend['sentence']
    if not word or not sentence_text:
        return jsonify({'error': 'word or sentence is empty'}), 400
    data, list_key = load_json()
    for index, entry in enumerate(data):
        if entry['key'] == word:
            number_sentences = len(data[index]['sentences'])
            sentence_audio_path = f"backend/audios/sentences/{word}_sentence_{number_sentences + 1}.mp3"
            sentence = {'sentence': sentence_text, 'audio': sentence_audio_path}
            data[index]['sentences'].append(sentence)
            data[index]['number'] -= 1
            save_json(data)
            if not os.path.exists(sentence_audio_path):
                tts = gTTS(text=sentence_text, lang='en')
                tts.save(sentence_audio_path)
            return jsonify({'ok': True}), 201
    return jsonify({'error': 'word not found in database'}), 404


@app.route('/words', methods = ['POST'])


def add_entry():
    data_from_frontend = request.get_json()
    word = (data_from_frontend['word'] or '').strip()

    if not word:
        return jsonify({'error': 'word is empty'}), 400
    
    data, list_key = load_json()
    if word in list_key:
        for index, entry in enumerate(data):
            if entry['key'] == word:
                data[index]['number'] +=1 
                save_json(data)
                return jsonify({'ok': True, 'total': len(data)}), 201
    else:
        entry = {}
        entry['key'] = word
        entry['number'] = 5
        entry['audio'] = f'backend/audios/words/{word}.mp3'
        entry['sentences'] = []
        data.append(entry)

        if not os.path.exists(entry['audio']):
            tts = gTTS(text = word, lang='en')
            tts.save(entry['audio'])
        save_json(data)
        return jsonify({'ok': True, 'total': len(data)}), 201

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
