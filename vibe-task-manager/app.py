from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Vibe Task Manager by Emtee-dev</h1><p>Projeto para XD Angola</p>"

@app.route("/api/tasks")
def tasks():
    return jsonify([{"id":1,"task":"Aprender Vibe Coding"}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
