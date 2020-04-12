from random import randint
import random
random.seed(1)
random_temperatures = [randint(30,101) for num in range(0, 50)]
perfect_customers = [3*temp + 10 for temp in random_temperatures]


temperature_inputs = [[temperature] for temperature in random_temperatures]
from sklearn.linear_model import LinearRegression
perfect_model = LinearRegression()
perfect_model.fit(temperature_inputs, perfect_customers)