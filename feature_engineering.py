#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def prepare_features(df):

    df = df.copy()

    # Fill missing
    df['Text1'] = df['Text1'].fillna("")
    df['Text2'] = df['Text2'].fillna("")

    # Clean function
    def clean_text(text):
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    df['Text1'] = df['Text1'].apply(clean_text)
    df['Text2'] = df['Text2'].apply(clean_text)

    # TF-IDF on combined corpus
    tfidf = TfidfVectorizer()
    tfidf.fit(pd.concat([df['Text1'], df['Text2']]))

    X1_tfidf = tfidf.transform(df['Text1'])
    X2_tfidf = tfidf.transform(df['Text2'])

    cosine_scores = [
        cosine_similarity(X1_tfidf[i], X2_tfidf[i])[0][0]
        for i in range(X1_tfidf.shape[0])
    ]

    return pd.DataFrame(cosine_scores)


# In[ ]:




