# Online Assignment Plagiarism Dataset

This dataset contains 150 pairs of assignment texts labeled for plagiarism detection. I am working on collecting more dataset. The model is trained to detect plagiarism between an uploaded file with the stored documents using pipeline of TF-IDF, Cosine similarity and Logistic Regression model. 
Database = PostgreSQL (Supabase)
Docker
Render (Deployment)

## Columns
- **text1**: First assignment text
- **text2**: Second assignment text
- **label**: 1 if plagiarized, 0 if not# assignment-plagiarism-dataset
- You can load the dataset in Python using pandas:

Folder Structure
project/
│
├── app.py
├── model.pkl
├── requirements.txt
├── Dockerfile
├── templates/
│   └── index.html
└── README.md

## How to Run Locally

1. Clone the repository
   git clone <your repo link>

2. Navigate into project
   cd plagiarism-checker

3. Create virtual environment
   python -m venv venv
   source venv/bin/activate   (Mac/Linux)
   venv\Scripts\activate      (Windows)

4. Install dependencies
   pip install -r requirements.txt

5. Set environment variable
   Create a .env file and add:

   DATABASE_URL=https://lkodbmuqmmmvqyprpkyq.supabase.co

6. Run the application
   python app.py

7. Open in browser:
   http://127.0.0.1:5000










## Model Training

The model was trained using:
- Custom feature engineering via FunctionTransformer
- TF-IDF cosine similarity
- Logistic Regression classifier

Model saved as model.pkl using joblib.

## Deployment

Application is deployed on Render using Docker runtime.
Database hosted on Supabase (PostgreSQL).
