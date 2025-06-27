from flask import Flask, request, jsonify
from flask_cors import CORS  # 👈 NEW

from scraper import scrape_all

app = Flask(__name__)
CORS(app)  # 👈 NEW

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    results = scrape_all(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
