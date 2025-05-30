import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
#
# model = Sequential()
# model.add(Dense(1, activation='linear'))
# #model.add(Dense(1, activation='linear'))
# #model.add(Dense(1, activation='linear'))
# model.add(Dense(1, activation='linear'))
#
# model.compile(optimizer='rmsprop', loss='mse')

df = pd.read_csv('Dane/f-c.csv', usecols=[1,2])

result = model.fit(df.F, df.C, epochs=1000, verbose=2)
df1 = pd.DataFrame(result.history)
print(df1)
df1.plot()
plt.show()

C_pred = model.predict(df.F)
plt.scatter(df.F, df.C)
plt.plot(df.F, C_pred)
plt.show()