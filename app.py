import json
from flask_cors import CORS
from flask import Flask, jsonify, request,send_file
import os
app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads/'
# @app.route('/hai')
# def hello():
#     return 'heloooo!!!!'
transcriptionData = [
  { "text": "The stale smell of old beer lingers.", "start": 1, "end": 4 },
  { "text": "it takes heat to bring out the odor.", "start": 4, "end": 6 },
  { "text": "A cold dip restores health and zest.", "start": 6, "end": 9 },
  { "text": "A salt pickle tastes fine with ham.", "start": 9, "end": 12 },
  { "text": "lacos al pastor are my ravorite", "start": 12, "end": 19 }
];

@app.route('/api/trial',methods=['POST'])
def recived():
    # print(request.json)
    f = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
    f.save(file_path)
    if f:
        print(f.filename)
        return jsonify({"data":transcriptionData,"file_path": file_path})\
        
@app.route('/api/get-audio/<path:file_path>')
def get_audio(file_path):
    return send_file(file_path)
if (__name__ == '__main__'):
    app.run(port=8000)
