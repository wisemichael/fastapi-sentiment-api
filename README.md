# FastAPI Sentiment API

This FastAPI application exposes endpoints for sentiment analysis and returning random movie reviews.

## Endpoints

- `GET /`  
  Returns a welcome message to confirm the API is running.

- `GET /predict`  
  Loads the IMDB dataset and returns sentiment predictions using a simple model.

- `GET /example`  
  Returns a random review from `example_data.json`.

## How to Run the App Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
