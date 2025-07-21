import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

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
file_path = "/home/aaron/Downloads/NHIS_Adult_Summary_Health_Statistics.csv"
df = pd.read_csv(file_path)

# properly loaded, now how will we decide on what to "clean"
