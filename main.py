from fastapi import FastAPI
from pydantic import BaseModel
import json
import random

# Import your sentiment prediction functions
from app.model import predict_sentiment, predict_sentiment_proba

# Initialize FastAPI app
app = FastAPI()

# Load example reviews from JSON
with open("example_data.json", "r") as f:
    reviews = json.load(f)

# Define the request schema using Pydantic
class TextInput(BaseModel):
    text: str

# Optional: Root endpoint (to avoid "Not Found" on `/`)
@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment API. Go to /docs for Swagger UI."}

# 1. Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# 2. Predict Sentiment Endpoint
@app.post("/predict")
def predict_sentiment_endpoint(input: TextInput):
    sentiment = predict_sentiment(input.text)
    return {"sentiment": sentiment}

# 3. Predict with Probability Endpoint
@app.post("/predict_proba")
def predict_with_proba(input: TextInput):
    result = predict_sentiment_proba(input.text)
    return {
        "sentiment": result["sentiment"],
        "probability": result["probability"]
    }

# 4. Get Example Review Endpoint
@app.get("/example")
def get_example():
    try:
        with open("example_data.json", "r") as f:
            data = json.load(f)
        review = random.choice(data["reviews"])
        return {"review": review}
    except Exception as e:
        return {"error": str(e)}


