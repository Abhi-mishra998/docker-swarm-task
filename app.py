from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/api")
def home():
    return jsonify({
        "msg": "Welcome to the backend by Abhishek Mishra",
        "host": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

