import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('Dane//diabetes.csv')
print(df.describe().T.to_string())

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi', 'diabetespedigreefunction', 'age']:
    df[col].replace(0, np.nan, inplace=True)
    mean_ = df[col].mean()
    df[col].replace(np.nan, mean_, inplace=True)

print(f'\nPo czyszczeniu:\n{df.describe().T.to_string()}')
df.to_csv('Dane//cukrzyca.csv', index=False)

X = df.iloc[ : , :-1]
y = df.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(f'Dokładność modelu to: {model.score(X_test, y_test)}')
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print(df.outcome.value_counts())

df1 = df.query("outcome==0").sample(n=500)
df2 = df.query("outcome==1").sample(n=500)
df3 = pd.concat([df1, df2])

X = df3.iloc[ : , :-1]
y = df3.outcome
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
print(f'Dokładność modelu to: {model.score(X_test, y_test)}')
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))