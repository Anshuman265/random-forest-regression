# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

# Training the Random forest regression model on the whole dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators= 10, random_state= 0)
regressor.fit(X,y)

print(regressor.predict([[6.5]]))

# Visualising the Random Forest Regression results (Higher Resolution)
X_grid = np.arange(min(X),max(X),0.01)
X_grid = X_grid.reshape((len(X_grid)),1)
plt.scatter(X,y,color = 'red')
plt.plot(X_grid,regressor.predict(X_grid),color = 'blue')
plt.title('Random Forest Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
