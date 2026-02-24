<p>1. Introduction</p>
<p>2. Architecture Diagram</p>
<p>3. Tech Stack</p>
<p>4. System Workflow</p>
<p>5. ML Pipeline Overview</p>
<p>6. Deployment Architecture</p>
<p>7. Future Improvements</p>





<h1>1️⃣ Introduction</h1>
<p><h2> 1.1 Purpose</h2>
Project: Online Assignment Plagiarism Detection System</p>

<p>
This system is designed to detect plagiarism in user-submitted assignment documents by comparing them against previously stored assignments using a machine learning model. 
The outcome is forecasted in the form of plagiarism level: High Plagiarism, Low Similarity & Moderate Similarity, along with the plagiarism percentage. The system accepts user-uploaded files
(.txt, .docx, .pdf), PostgreSQL for storage purpose and cloud-hosted deployment.

<h2>1.2 Scope</h2>

This project is designed for:

Academic institutions

Internship assignments

Educational platforms

Online submission portals

<h1>2️⃣ Architecture Diagram</h1>

Here’s the high-level architecture of the system:

          +----------------+
          |     User       |
          | (Browser/PC)   |
          +-------+--------+
                  |
                  v
          +----------------+
          |  Flask Web App |
          |  (app.py)      |
          +-------+--------+
                  |
                  v
     +-------------------------+
     | File Processing Module  |
     | - .txt / .docx / .pdf   |
     | - Text extraction       |
     +------------+------------+
                  |
                  v
     +-------------------------+
     | Feature Engineering     |
     | - TF-IDF vectorization  |
     | - Cosine similarity     |
     +------------+------------+
                  |
                  v
     +-------------------------+
     | Machine Learning Model  |
     | - Logistic Regression   |
     | - Predicts plagiarism % |
     +------------+------------+
                  |
                  v
     +-------------------------+
     | PostgreSQL Database     |
     | (Supabase Cloud)        |
     | - Stores previous files |
     +-------------------------+
                 |
                 v
         +----------------+
         | User Interface |
         | Shows Result   |
         +----------------+

<h3>Explanation:</h3>

1. Users upload assignment files via the web interface.

2. Flask backend validates the file type and extracts text.

3. Text is compared with existing assignment files stored in PostgreSQL.

4. Feature engineering converts text into numerical similarity scores.

5. Logistic Regression model predicts plagiarism probability.

6. Result is stored in the database and displayed to the user.
  
<h1>3️⃣ Technology Stack</h1>


<h2>Layer	  -----------------------------Technology / Tool	 ------------------>        Purpose</h2>

Backend    -------------------------------------------->      Python, Flask, Gunicorn  -------------------->   Web server, request handling, WSGI deployment

Machine Learning  ------------------------------------>  scikit-learn, TF-IDF, Logistic Regression	--------------->  Feature extraction and plagiarism prediction

Database	-------------------------------------------->      PostgreSQL (Supabase Cloud)  ------------------------>   Stores uploaded assignments and text content

File Processing -------------------------------------->         python-docx, PyPDF2	 ----------------------------->  Extract text from .docx and .pdf files

Frontend	-------------------------------------------->        HTML + Jinja2 templates	--------------------------->  User interface for file upload and displaying results

Deployment	------------------------------------------>          Docker, Render	 ---------------------------------->  Containerized cloud deployment

Version Control	-------------------------------------->            GitHub


<h1>4️⃣ System Workflow</h1>

The system follows a sequential workflow from file upload to plagiarism prediction and storage.

<h2>Step 1: File Upload</h2>

The user uploads an assignment file through the web interface.

Supported formats:

.txt

.docx

.pdf

The file is received by the Flask backend via an HTTP POST request.

<h2>Step 2: File Validation & Text Extraction</h2>

The system validates the file format.

Based on file type, appropriate extraction method is used:

.txt → decoded as UTF-8 text

.docx → extracted using python-docx

.pdf → extracted using PyPDF2

If the format is unsupported, an error message is returned to the user.

<h2>Step 3: Fetch Existing Assignment Data</h2>

The system retrieves previously stored assignment texts from the PostgreSQL database. These stored records act as reference documents for plagiarism comparison.

<h2>Step 4: Dataset Preparation</h2>

A comparison dataset is created dynamically:

Text1 → the uploaded assignment (repeated for each stored record)

Text2 → each stored assignment text

This enables pairwise similarity comparison between the new submission and all existing assignments.

<h2>Step 5: Feature Engineering</h2>

The system processes text data as follows:

a. Text cleaning (lowercasing, removing special characters)

b. TF-IDF vectorization

c. Cosine similarity computation

The output is a numerical similarity score for each comparison pair.

<h2>Step 6: Machine Learning Prediction</h2>

The similarity features are passed to the trained Logistic Regression model. The model predicts the probability of plagiarism.
The highest probability score is selected as the final plagiarism percentage.

<h2>Step 7: Store New Submission</h2>

The uploaded assignment text is inserted into the database. This ensures it can be used for future plagiarism checks.

<h2>Step 8: Result Display</h2>

The plagiarism percentage is returned to the user. The frontend displays the result in a readable format.
Proper error messages are shown for invalid files or processing failures.

<h1>5️⃣ ML Pipeline Overview</h1>

The Machine Learning pipeline is responsible for transforming raw text into numerical features and predicting plagiarism probability using a trained classification model.

<h2>5.1 Data Input</h2>

The pipeline receives:

a. Extracted text from the uploaded assignment

b. Previously stored assignment texts from the database

c. Each new submission is compared against all existing assignments.

<h2>5.2 Text Preprocessing</h2>

Before feature extraction, the text undergoes preprocessing:

a. Convert text to lowercase

b. Remove special characters and punctuation

c. Remove extra whitespace

d. Handle missing values (if any)

This ensures uniform representation and improves vectorization quality.

<h2>5.3 Feature Extraction (TF-IDF)</h2>

The system uses TF-IDF (Term Frequency – Inverse Document Frequency) to convert text into numerical vectors.

TF-IDF helps:

a. Capture word importance

b. Reduce impact of very common words

c. Represent documents as feature vectors

d. Each document is transformed into a high-dimensional sparse vector.

<h2>5.4 Similarity Computation</h2>

After vectorization:

Cosine Similarity is computed between:

a. Uploaded assignment vector

b. Each stored assignment vector

Cosine similarity measures the angle between vectors and returns a value between:

0 → Completely different

1 → Identical

These similarity scores act as input features for the classification model.

<h2>5.5 Model Prediction</h2>

Model Used: Logistic Regression

Why Logistic Regression?

a. Simple and interpretable

b. Suitable for binary classification

c. Outputs probability scores

The model:

Takes similarity features as input

Predicts probability of plagiarism

Outputs a value between 0 and 1

The highest probability score is selected as the final plagiarism percentage.

<h2>5.6 Output</h2>

The final output includes:

Plagiarism probability (converted to percentage)

Stored record for future comparisons

<h2>ML Pipeline Summary Flow</h2>
Raw Text
   ↓
Text Cleaning
   ↓
TF-IDF Vectorization
   ↓
Cosine Similarity
   ↓
Logistic Regression Model
   ↓
Plagiarism Probability (%)


  
</p>
