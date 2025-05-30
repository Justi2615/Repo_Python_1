import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('Dane\\iris.csv')
print(df['class'].value_counts())

species = {
    'Iris-setosa':0, 'Iris-versicolor': 1, 'Iris-virginica': 2
}

df['class_value'] = df['class'].map(species)
print(df.to_string())

sample = [5.6, 3.2, 5.2, 1.45]

#sns.scatterplot(data=df, x='sepallength', y='sepalwidth', hue='class')
#plt.scatter(5.6, 3.2, c='r')
#plt.show()

#sns.scatterplot(data=df, x='petallength', y='petalwidth', hue='class')
#plt.scatter(5.2, 1.45, c='r')
#plt.show()

X = df.iloc[ : , :-2]
y = df.class_value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = KNeighborsClassifier(n_neighbors=5, weights='uniform')
model.fit(X_train, y_train)
print(f'Dokładność modelu to: {model.score(X_test, y_test)}')
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

results = []
for k in range (1, 101):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    results.append(model.score(X_test, y_test))

plt.plot(range(1, 101), results)
plt.show()