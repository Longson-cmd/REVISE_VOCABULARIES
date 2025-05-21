from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

@app.route('/get_sentence')
def get_sentence():
    return jsonify ({
        'text' : 'I eat breakfast', 
        'audio_path': '/audios/sentences/eat_sentence_1.mp3'
    })


@app.route('/audios/<path:filename>')
def server_audios(filename):
    audios_folder = os.path.join(app.root_path, 'audios')
    return send_from_directory(audios_folder, filename)
if __name__ == "__main__":
    app.run()

# C:\Users\PC\Desktop\Practise\backend\audios\sentences\eat_sentence_2.mp3