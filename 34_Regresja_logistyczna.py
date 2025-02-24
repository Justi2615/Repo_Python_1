from operator import concat

import pandas as pd
from mlxtend.evaluate import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('Dane_po_obróbce/cukrzyca.csv', sep=';')
print(df.iloc[2,4])
print(df.iloc[2:4, 4:6])

X = df.iloc[ : , :-1]
y = df.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(f'Dokładność modelu to: {model.score(X_test, y_test)}')
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print(df.outcome.value_counts())

df1 = df.query('outcome==0').sample(n=500)
df2 = df.query('outcome==1').sample(n=500)
df3 = pd.concat([df1, df2])