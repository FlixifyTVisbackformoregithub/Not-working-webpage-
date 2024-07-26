from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_proxy():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400

    response = requests.get(f"https://www.google.com/search", params={"q": query})
    
    if response.status_code != 200:
        return jsonify({"error": "Search failed"}), 500

    return response.text

if __name__ == '__main__':
    app.run(port=5000)
