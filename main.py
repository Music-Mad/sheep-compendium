from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    return db.get_sheep(id)

@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    db.data[sheep.id] = sheep
    return sheep

@app.put("/sheep/{id}", response_model=Sheep)
def put_sheep(sheep: Sheep):
    if sheep.id not in db.data:
        raise HTTPException(status_code=400, detail="Sheep ID does not exist in database")

    db.data[sheep.id] = sheep
    return sheep

@app.delete("/sheep/{id}", response_model=Sheep)
def delete_sheep(id: int):
    sheep = db.data[id]
    del db.data[id]
    return sheep





