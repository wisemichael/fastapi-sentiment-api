import pickle
import os

# Load the trained sentiment model.
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'sentiment_model.pkl')
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

# app/model.py predict and probability functions.

from typing import Dict

positive_words = {"good", "great", "fantastic", "amazing", "enjoyed", "love", "excellent", "awesome", "nice"}
negative_words = {"bad", "terrible", "awful", "boring", "poor", "hate", "worst", "disappointing", "lame"}

def predict_sentiment(text: str) -> str:
    text = text.lower()
    pos_count = sum(word in text for word in positive_words)
    neg_count = sum(word in text for word in negative_words)

    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    else:
        return "neutral"  # fallback if uncertain


def predict_sentiment_proba(text: str) -> Dict:
    sentiment = predict_sentiment(text)

    if sentiment == "positive":
        probability = 0.9
    elif sentiment == "negative":
        probability = 0.85
    else:
        probability = 0.6

    return {"sentiment": sentiment, "probability": round(probability, 4)}
