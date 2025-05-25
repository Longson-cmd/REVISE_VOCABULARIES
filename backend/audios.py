import os
import json
from gtts import gTTS

with open('backend/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

os.makedirs('backend/audios/words', exist_ok=True)
os.makedirs('backend/audios/sentences', exist_ok=True)

data_convert = data
for entry in data_convert:
    word = entry['key']
    audio_word_path = entry['audio']

    if not os.path.exists(audio_word_path):
        tts = gTTS(text=word, lang='en')
        tts.save(audio_word_path)

    sentences = entry['sentences']
    for index, sentence_data in enumerate(sentences):
        sentence = sentence_data['sentence']
        audio_sentence_path = sentence_data['audio']

        if not os.path.exists(audio_sentence_path):
            tts = gTTS(text = sentence, lang='en')
            tts.save(audio_sentence_path)
        
# 'backend/audios/words'

print("✅ All audio files generated successfully!")
