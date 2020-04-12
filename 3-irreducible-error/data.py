from graph import trace_values
from random import randint, seed
seed(1)

random_temperatures = list(map(lambda num: randint(30,101), range(0, 50)))
perfect_customers = list(map(lambda temp: 3*temp + 10, random_temperatures))



from sklearn.linear_model import LinearRegression
perfect_model = LinearRegression()
temperature_inputs = list(map(lambda temperature: [temperature], random_temperatures))
perfect_model.fit(temperature_inputs, perfect_customers)

random_errors = [randint(-30,30) for num in range(0, 50)]
customers_zipped_errors = list(zip(perfect_customers, random_errors))
customers_with_errors = [customer + error for customer, error in customers_zipped_errors] 

data_trace = trace_values(random_temperatures, customers_with_errors, name = 'data with randomness')