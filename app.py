from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"msg": "Hello from backend Make by Abhishek Mishra just for testing"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
