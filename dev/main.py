import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import re

pd.set_option('display.max_colwidth', None)


# practicing "train_test_split"

"""
Notes:
sklearn.model_selection.train_test_split
(*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None)

parameters:
    - all arrays must have the same shape[0]/length
        - intakes lists, np.array, scipy-sparse matrices, pd.df
    
    - test_size: float or int, default=None
        - if float, should be between 0.0<=x<=1.0 representing proportion of
          dataset to include in TEST SPLIT
        - if None, it's default is set to complement of train_size
            - if train_size is none, it's set to 0.25
    
    - train_size: float or int, default=None
        - similarly, should be between 0.0 and 1.0 representing the proporition of the dataset to include in the training split.
          if set to none, will be set to complement of the test size

    - random_state: int, RandomState instance or None, default=None
        - controls shuffling, pass in an integer to create a reproducible output across function calls

    - shuffle : bool, default=True
        - if yes, data is shuffled before splitting, if false, then stratify must be none
    
    - stratify : array-like, default=None
        - if !=None, data is split into stratified fashion, using this as the class labels

"""

# importing file
file_path = "NHIS_Adult_Summary_Health_Statistics.csv"
df = pd.read_csv(file_path)

# properly loaded, now how will we decide on what to "clean"
description = df['Description']

'''
To reduce string processing overhead, we can just reduce the description dataset prior to string parsing.
We'll first remove all "NaN" columns.
'''
description = description.dropna().to_string()

description_list = description.strip().split("\n")
# pattern = r" that they had\s+(.+)"

# results = [match for text in description_list for match in re.findall(pattern, text, re.IGNORECASE)]
# print(results)

# print(description_list[4152].strip())
ailments = {}
for text in description_list:
    cleaned_text = re.sub(r'^\d+\s+', '', text)
    pattern = r"that they had\s+(.+?)\."
    matches = re.findall(pattern, cleaned_text, re.IGNORECASE)
    if matches:
        if matches[0] in ailments:
            print(ailments.get(matches[0]))
        else:
            ailments.update({matches[0], 1})
    else:
        continue
    

print(ailments)