# Syntax
All Syntax that I may need for future. (Probably won't. Just google it)

Libraries:
- Pandas: Helps load data frame to 2D array and perform actions on it
- Numpy: Very fast computational library for python
- Matplotlib/Seaborn: Used to draw visualization
- Sklearn: This model contains multiple libraries having pre-implemented functions to perform tasks from data preprocessing to model development and evaluation

## Category Variables:
Steps:
- Import necessary libraries
- Load dataset
- Make list of all correct categorical value
- use the list to remove bogus values or correct it if enough data
-
```py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.preprocessing import LabelEncoder

#
# create a new dataframe with possible values for blood type
blood_type_categories = pd.DataFrame({
	'blood_type': ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
})
blood_type_categories

```
