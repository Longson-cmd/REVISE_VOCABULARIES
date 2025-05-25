from flask import Flask, request, jsonify
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

FILE_3 = 'C:/Users/PC/Desktop/New folder/backend/self.json'
def load_json(FILE):
    with open(FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data
    
def save_json(FILE, data):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/self', methods = ['GET'])
def Get_data_self():
    data = load_json(FILE_3)
    return jsonify(data), 200


@app.route('/self', methods = ['PUT'])
def save_data_self():
    data_from_frontend = request.get_json()
    if not data_from_frontend:
        print('failed to update')
        return jsonify({'status': 'fail', 'message': 'No data received'}), 400
    else:
        save_json(FILE_3, data_from_frontend)
        return jsonify({'status': 'success', 'message': 'Data saved'}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)