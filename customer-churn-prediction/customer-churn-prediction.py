import numpy as np
import pandas as pd
import sys

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

# model = KNeighborsClassifier(n_neighbors=1)
model = GaussianNB()

data = pd.read_csv("./dataset/internet_service_churn.csv")
data1 = data.dropna()

columns = data1.columns.tolist()
columns.remove("churn")
columns.remove("id")

x = data1[columns].values
y = data1[["churn"]].values
y = np.ravel(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=True)
model.fit(x_train, y_train)
predictions = model.predict(x_test)

correct = (y_test == predictions).sum()
incorrect = (y_test != predictions).sum()
total = len(predictions)

print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")
