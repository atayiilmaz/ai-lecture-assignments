import numpy as np
import pandas as pd
import sys
from numpy import random
from random import randint
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("./dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv")
data = data.dropna()
data.replace({"No": 0, "Yes": 1}, inplace=True)
data.replace({"Male": 0, "Female": 1}, inplace=True)
data.replace({"No phone service": 0, "DSL":1, "Fiber optic": 1, "No internet service": 0, " ": 0}, inplace=True)

columns = data.columns.tolist()
columns.remove("Churn")
columns.remove("customerID")
columns.remove("PaymentMethod")
columns.remove("Contract")


# model = KNeighborsClassifier(n_neighbors=3)
model = GaussianNB()
min = 0
max = 0
y = data[["Churn"]].values
y = np.ravel(y)

for i in range(0, 1000):
    random_chosen_column = random.choice(columns, randint(1, len(columns)))
    x = data[random_chosen_column].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=True)
    if (len(x_train) != 0 and len(y_train) != 0):
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)

        correct = (y_test == predictions).sum()
        incorrect = (y_test != predictions).sum()

        acc = accuracy_score(y_test, predictions)
        if (i == 0):
            min = acc
            max = acc
        if (acc > max):
            max = acc
        if (acc < min):
            min = acc

print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: %.2f%%" %(max * 100))