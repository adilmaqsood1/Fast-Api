from fastapi.testclient import TestClient
from project.main import app 

def test_root_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_home_check():
    client = TestClient(app=app)
    response = client.get("/home")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to home page"}

    


    