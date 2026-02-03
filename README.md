# Online Assignment Plagiarism Dataset

This dataset contains 150 pairs of assignment texts labeled for plagiarism detection.

## Columns
- **text1**: First assignment text
- **text2**: Second assignment text
- **label**: 1 if plagiarized, 0 if not# assignment-plagiarism-dataset
- You can load the dataset in Python using pandas:

```python
import pandas as pd
df = pd.read_csv("data/plagiarism_data.csv")
