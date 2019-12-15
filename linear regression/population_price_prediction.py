import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
price_model = LinearRegression()
data = open("inputTrainingSet.txt","r")
population = []
price = []
for a in data:
    population.append(float(a.split(",")[0]))
    price.append(float(a.split(",")[1]))
    
x = np.array(population).reshape(-1,1)
y = np.array(price)
price_model.fit(x,y)
print("Score: ",price_model.score(x,y))
print("Intercept: ",price_model.intercept_)
print("Slope: ",price_model.coef_)
predict_price = price_model.predict(x)
print("Pridicted Prices: \n",predict_price.reshape(-1,1))