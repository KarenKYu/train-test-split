from random import randint, seed
import numpy as np
temps = np.array([30, 31, 32, 32, 33, 33, 33, 33, 38, 42, 42, 43, 45, 45, 47, 53, 56, 57, 58, 58, 59, 
59, 59, 62, 64, 67, 67, 70, 72, 74, 78, 78, 79, 83, 84, 84, 85, 86, 87, 87, 88, 90, 92, 93, 93, 94, 97, 99, 100, 101])

input_temps = temps.reshape(-1, 1)

is_weekends = [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1,0, 0, 0, 0,
0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0]

temps_and_is_weekends = np.array(list(zip(temps, is_weekends)))

seed(2)
random_ages = list(map(lambda num: randint(25,65), range(0, 50)))

temps_weekends_and_ages = np.array(list(zip(temps, is_weekends, random_ages)))

seed(2)
customers = np.array([100, 103, 146, 106, 109, 149, 149, 149, 164, 176, 176, 139, 
145, 185, 151, 209, 178, 181, 184, 184, 187, 187, 227, 196, 202, 211, 251, 260, 226,
232, 244, 284, 287, 259, 262, 262, 265, 268, 271, 271, 274, 320, 286, 289, 289, 332, 301, 347, 310, 313])
random_errors = np.array(list(map(lambda num: randint(-30,30), range(0, 50))))
customers_with_errors = np.array(list(map(lambda idx: customers[idx] + random_errors[idx],range(0, 50))))

from sklearn.linear_model import LinearRegression
feature_datasets = [input_temps, temps_and_is_weekends, temps_weekends_and_ages]
models = []
for dataset in feature_datasets:
    model = LinearRegression()
    model.fit(dataset, customers_with_errors)
    models.append(model)
models

intercepts = [model.intercept_ for model in models]
intercepts
# [35.62031572335471, 9.854773197812762, 12.155548281106803]

coefs = [model.coef_ for model in models]
coefs

def build_data_set(theta_1 = 3, theta_2 = 10, error_plus_minus = 50, size = 50):
    random_temperatures = list(map(lambda num: randint(30,101), range(0, size)))
    perfect_customers = list(map(lambda temp: theta_1*temp + theta_2, random_temperatures))
    random_errors = list(map(lambda num: randint(-error_plus_minus,error_plus_minus), range(0, size)))
    zipped_customers = list(zip(perfect_customers, random_errors))
    noisy_customers = [perfect_customer + error for perfect_customer, error in zipped_customers]
    return np.array(list(zip(random_temperatures, noisy_customers)))

models_and_data = list(zip(models, feature_datasets))
predictions = list(map(lambda model_and_data: model_and_data[0].predict(model_and_data[1]), models_and_data))



