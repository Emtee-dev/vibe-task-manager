from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <body style="font-family:sans-serif; background:#0a0a0a; color:white; text-align:center; padding:50px;">
    <h1>🚀 Vibe Task Manager</h1>
    <h2>by Emtee-dev</h2>
    <p>Projeto criado com Vibe Coding + Flask + REST API</p>
    <p style="color:#00ff88;">Para XD Angola R&D - Luanda, Angola</p>
    <a href="/api/tasks" style="background:#00ff88; color:black; padding:10px 20px; text-decoration:none; border-radius:5px;">Ver API REST</a>
    </body>
    """
@app.route("/api/tasks")
def tasks():
    return jsonify([
        {"id":1,"task":"Aprender Vibe Coding","status":"feito"},
        {"id":2,"task":"Criar portfolio para XD Angola","status":"feito"},
        {"id":3,"task":"Conseguir vaga","status":"em progresso"}
    ])
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
