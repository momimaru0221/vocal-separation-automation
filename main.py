# main.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, from the app via Flask!"


if __name__ == "__main__":
    # Flaskの開発サーバーをポート8000で起動
    app.run(host="0.0.0.0", port=8000)
