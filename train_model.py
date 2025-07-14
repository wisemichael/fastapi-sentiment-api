import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# 1. Loads dataset (IMDB)
df = pd.read_csv("IMDB_Dataset/IMDB Dataset.csv")

# 2. Preprocess
df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # Shuffle
df = df.head(10000)  

# 3. Train/test split
X = df["review"]
y = df["sentiment"]

# 4. Convert labels to binary
y = y.map({"positive": 1, "negative": 0})

# 5. Create pipeline
model = make_pipeline(CountVectorizer(), MultinomialNB())

# 6. Train the model
model.fit(X, y)

# 7. Save the model as 'sentiment_model.pkl'
with open("sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully as 'sentiment_model.pkl'")
