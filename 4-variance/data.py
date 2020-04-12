import numpy as np
from random import randint

def build_data_set(theta_1 = 3, theta_2 = 10, error_plus_minus = 50, size = 50):
    random_temperatures = list(map(lambda num: randint(30,101), range(0, size)))
    perfect_customers = list(map(lambda temp: theta_1*temp + theta_2, random_temperatures))
    random_errors = list(map(lambda num: randint(-error_plus_minus,error_plus_minus), range(0, size)))
    zipped_customers = list(zip(perfect_customers, random_errors))
    noisy_customers = [perfect_customer + error for perfect_customer, error in zipped_customers]
    return np.array(list(zip(random_temperatures, noisy_customers)))

dataset = build_data_set()
temperatures = dataset[:, 0]
noisy_customers = dataset[:, 1]

from sklearn.linear_model import LinearRegression
initial_model = LinearRegression()
initial_model.fit(temperatures.reshape(-1, 1), noisy_customers)