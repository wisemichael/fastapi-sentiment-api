This project is a simple sentiment analysis API built using FastAPI. It utilizes a machine learning pipeline with scikit-learn to classify IMDB movie reviews as either positive or negative.

Model
Vectorizer: CountVectorizer

Classifier: Multinomial Naive Bayes

Dataset: IMDB movie reviews (10,000 samples)

Output: A trained .pkl file (sentiment_model.pkl)

Project Structure
.
├── app/
│ ├── init.py
│ ├── api.py
│ ├── data_loader.py
│ └── model.py
├── IMDB_Dataset/
│ └── IMDB_Dataset.csv
├── dockerfile
├── example_data.json
├── main.py
├── makefile
├── README.md
├── requirements.txt
├── sentiment_model.pkl
└── train_model.py

Running the API Locally
Install dependencies:
pip install -r requirements.txt

Train the model:
python train_model.py

Start the FastAPI server:
uvicorn main:app --reload

Then open your browser and go to:
http://127.0.0.1:8000/docs
This is the interactive FastAPI documentation page where you can test the endpoints.
