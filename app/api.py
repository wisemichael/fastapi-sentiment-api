from fastapi import APIRouter
from app.data_loader import load_imdb_dataset
from app.model import simple_model
import json
import random

router = APIRouter()

with open("example_data.json") as f:
    data = json.load(f)
    reviews = data["reviews"]

@router.get("/example")
def get_example():
    return {"review": random.choice(reviews)}

@router.get("/")
def read_root():
    return {"message": "Hello! FastAPI is working"}

@router.get("/predict")
def predict():
    data = load_imdb_dataset()
    result = simple_model(data)
    return result
