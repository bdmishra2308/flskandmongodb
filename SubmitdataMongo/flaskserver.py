from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Connect to MongoDB Atlas
client = MongoClient("mongodb://localhost:27017/")
db = client["Dev"]
collection = db["test"]

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.json
        collection.insert_one(data)
        return jsonify({"message": "Data submitted successfully", "redirect": True})
    except Exception as e:
        return jsonify({"error": str(e), "redirect": False})

if __name__ == '__main__':
    app.run(debug=True, port=5000)