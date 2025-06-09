from flask import Flask, jsonify
import json

app = Flask(__name__)

def read_data():
    """Reads data from the backend JSON file."""
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

@app.route('/api', methods=['GET'])
def api_route():
    """Returns the JSON data from the backend file."""
    data = read_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
