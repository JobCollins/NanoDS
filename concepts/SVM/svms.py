from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

data = np.asarray(pd.read_csv('data.csv', header=None))

# assign features to variable X, and labels to variable y
X = data[:, 0:2]
y = data[:,2]

# create the svm model
model = SVC(kernel='rbf', gamma=27)

# fit the model
model.fit(X, y)

# predict
y_pred = model.predict(X)

# calculate accuracy
acc = accuracy_score(y, y_pred)