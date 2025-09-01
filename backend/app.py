# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from ai_models.ai_models import predict_fraud
from backend.db import insert_cert, get_all_certs   # import from backend/db.py

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if not data:
        return jsonify({"error": "No input data"}), 400
    result = predict_fraud(data)
    return jsonify(result), 200

@app.route("/test-db")
def test_db():
    from backend.db import get_all_certs
    try:
        certs = get_all_certs()
        return jsonify({"db_status": "connected", "certs": certs})
    except Exception as e:
        return jsonify({"db_status": "error", "error": str(e)})


@app.route("/ping")
def ping():
    return jsonify({"status": "ok"})

# Add a certificate (POST)
@app.route("/certificates", methods=["POST"])
def add_certificate():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    cert_id = insert_cert(data)
    return jsonify({"status": "inserted", "id": str(cert_id)}), 201

# Get all certificates (GET)
@app.route("/certificates", methods=["GET"])
def list_certificates():
    certs = get_all_certs()
    return jsonify(certs), 200

if __name__ == "__main__":
    app.run(debug=True)
