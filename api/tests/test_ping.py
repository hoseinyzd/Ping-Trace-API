import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


from fastapi.testclient import TestClient
from api.main import app



client = TestClient(app)

def test_ping_google():
    response = client.get("/ping/8.8.8.8")
    assert response.status_code == 200
    assert "reachable" in response.json()
