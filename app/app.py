from flask import Flask, jsonify
import datetime
import os
import sys

app = Flask(__name__)

# Required environment variables
DB_URL = os.environ.get("DATABASE_URL")
if not DB_URL:
    print("ERROR: DATABASE_URL environment variable is required.")
    sys.exit(1)

VERSION = os.environ.get("VERSION", "2.0.0")

@app.route("/")
def home():
    return jsonify({
        "app" : "automate-deploy-platform",
        "version" : VERSION,
        "status" : "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status" : "healthy",
        "version" : VERSION,
        "timestamp" : datetime.datetime.now().isoformat()
    })

@app.route("/api/status")
def status():
    return jsonify({
        "status" : "ok",
        "version" : VERSION,
        "environment" : os.environ.get("APP_ENV", "development"),
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True)