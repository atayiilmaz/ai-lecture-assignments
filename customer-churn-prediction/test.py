import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

search_space = {
    'var_smoothing': np.logspace(0,-9, num=100)
}

def objective_function(x_train, y_train, x_test, y_test, params):
    model = GaussianNB(var_smoothing=params['var_smoothing'])
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    correct = (y_test == predictions).sum()
    return correct

data = pd.read_csv("./dataset/internet_service_churn.csv")
data1 = data.dropna()
columns = data1.columns.tolist()
columns.remove("churn")
columns.remove("id")
x = data1[columns].values
y = data1[["churn"]].values
y = np.ravel(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=True)
current_solution = {'var_smoothing': 1}

while True:
    fitness = objective_function(x_train, y_train, x_test, y_test, current_solution)
    neighbors = []
    for k in search_space.keys():
        for v in search_space[k]:
            neighbor = current_solution.copy()
            neighbor[k] = v
            neighbors.append(neighbor)
    best_neighbor = current_solution
    for neighbor in neighbors:
        neighbor_fitness = objective_function(x_train, y_train, x_test, y_test, neighbor)
        if neighbor_fitness > fitness:
            best_neighbor = neighbor
            fitness = neighbor_fitness
    if best_neighbor == current_solution:
        break
    current_solution = best_neighbor

model = GaussianNB(var_smoothing=current_solution['var_smoothing'])
model.fit(x_train, y_train)
predictions = model.predict(x_test)
correct = (y_test == predictions).sum()
incorrect = (y_test != predictions).sum()
total = len(predictions)
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")