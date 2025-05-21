from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/get-eat-audio')  # Create a route for the specific audio file
def get_eat_audio():
    audio_folder = os.path.join(app.root_path, 'audios', 'sentences')  # Path to the folder
    filename = 'eat_sentence_1.mp3'  # Only serve this file
    return send_from_directory(audio_folder, filename)  # Serve the file

if __name__ == '__main__':
    app.run(debug=True)
