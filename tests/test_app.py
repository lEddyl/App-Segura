from src.app import app

def test_root_ok():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert r.get_json() == {"msg": "Hola, mundo seguro"}
