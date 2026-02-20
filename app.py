#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from feature_engineering import prepare_features
import pandas as pd
import os
import psycopg2
import joblib
import re





app = Flask(__name__)

# Load your ML model
model = joblib.load("model.pkl")

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    "postgresql://postgres.lkodbmuqmmmvqyprpkyq:plagiarism-detector-done@aws-1-ap-south-1.pooler.supabase.com:6543/postgres"
)
cursor = conn.cursor()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    from docx import Document
    import io

    file = request.files["file"]
    filename = secure_filename(file.filename)

    if filename.endswith(".docx"):
       doc = Document(io.BytesIO(file.read()))
       text = "\n".join([para.text for para in doc.paragraphs])

    elif filename.endswith(".txt"):
        text = file.read().decode("utf-8", errors="ignore")

    else:
        return render_template("index.html", prediction_text="Unsupported file format.")




# Fetching all the existing texts
    cursor.execute("SELECT text_content FROM assignment_files")
    rows = cursor.fetchall()
    existing_texts = [r[0] for r in rows]

    conn.commit()

    import pandas as pd

    df = pd.DataFrame({
    'Text1': [text] * len(existing_texts),  # uploaded file repeated
    'Text2': existing_texts                  # each previous assignment
     })


# Inserting the text into existing table in the database
    cursor.execute(
    """
    INSERT INTO assignment_files (file_name, text_content)
    VALUES (%s, %s)
    """,
    (filename, text)
      )

    conn.commit()

    # --- Predict plagiarism ---
    prediction = model.predict(df)
    probability = model.predict_proba(df)

    plagiarism_scores = probability[:, 1] * 100
    plagiarism_percent = round(max(plagiarism_scores), 2)





    # --- Return result to template ---
    #result = f"Plagiarism Detected – {plagiarism_percent}%"
    if plagiarism_percent >= 70:
        result = f"High Plagiarism – {plagiarism_percent}%"
    elif plagiarism_percent >= 40:
        result = f"Moderate Similarity – {plagiarism_percent}%"
    else:
        result = f"Low Similarity – {plagiarism_percent}%"

    return render_template("index.html", prediction_text=result)


if __name__ == "__main__":
    app.run(debug=True)




