# main.py
import os
from flask import Flask


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    @app.route("/")
    def hello():
        """Return a simple greeting."""
        return "Hello from Flask inside Docker!"

    return app


if __name__ == "__main__":
    # 環境変数でホスト・ポート指定（デフォルトは0.0.0.0:8000）
    HOST = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    PORT = int(os.environ.get("FLASK_RUN_PORT", "8000"))

    app = create_app()
    app.run(host=HOST, port=PORT)
