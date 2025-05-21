from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

import os
app = Flask(__name__)
CORS(app)

print(app.root_path)
@app.route('/get-sentence')
def get_sentence():
    return jsonify({
        "text": "I eat breakfast.",
        "audio_path": "backend/audios/sentences/eat_sentence_1.mp3" 
    })

# Endpoint to serve the audio file
@app.route('/backend/audios/sentences/<path:filename>')  # Define a route that matches any file path under /backend/audios/sentences/
def serve_audio_file(filename):  # Define a function that takes the requested filename as a parameter
    audio_folder = os.path.join(app.root_path, 'audios', 'sentences')  # Build the full path to the 'sentences' folder inside the 'audios' directory
    return send_from_directory(audio_folder, filename)  # Send the requested file from the 'sentences' folder back to the client


if __name__ == '__main__':
    app.run(debug=True)
