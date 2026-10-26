"""Backend Flask de la plantilla-app.

Arrancar con:  python3 app.py
Escucha en:    http://localhost:5000
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "app": "plantilla-app"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
