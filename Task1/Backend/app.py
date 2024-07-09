from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection details
client = MongoClient("mongodb://root:root@mongodb-service.mongodb-namespace.svc.cluster.local:27017")
db = client.test_database

@app.route('/')
def home():
    return "Hello, Flask is running!"

@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    if 'name' not in data or 'age' not in data:
        return jsonify({'error': 'Please provide name and age'}), 400
    
    record = {
        'name': data['name'],
        'age': data['age']
    }
    
    result = db.test_collection.insert_one(record)
    return jsonify({'inserted_id': str(result.inserted_id)})

@app.route('/get', methods=['GET'])
def get_records():
    records = list(db.test_collection.find())
    for record in records:
        record['_id'] = str(record['_id'])
    return jsonify(records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
