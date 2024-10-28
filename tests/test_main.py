from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200

    assert response.json() == {

        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():

    testSheep = {
        "id": 7,
        "name": "Suffolk",
        "breed": "Gotland",
        "sex": "ewe"
    }

    response = client.post("/sheep/", json={"id": 7, "name": "Suffolk", "breed": "Gotland", "sex": "ewe"})

    assert response.status_code == 201
    assert response.json() == testSheep

    response = client.get("/sheep/7")
    assert response.status_code == 200

    assert response.json() == testSheep



def test_put_sheep():
    response = client.put("/sheep/4", json={
        "id": 4,
        "name": "Spicy",
        "breed": "A cool breed",
        "sex": "ewe"
    })

    assert response.status_code == 200
    assert response.json() == {
        "id": 4,
        "name": "Spicy",
        "breed": "A cool breed",
        "sex": "ewe"
    }

def test_delete_sheep():
    response = client.delete("/sheep/1")

    assert response.status_code == 200
    assert response.json() == {

        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }
