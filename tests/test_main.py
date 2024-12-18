# tests/test_main.py
from main import create_app


def test_root_endpoint():
    """Test that the root endpoint returns the expected response."""
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello from Flask inside Docker!"
