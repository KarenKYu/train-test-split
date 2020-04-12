from random import randint, seed, choices
seed(2)
temps = list(range(0, 150))

input_temps = list(map(lambda temp: [temp], temps))
seed(2)
is_weekends = choices([0, 1], [5/7, 2/7], k = 150)

temps_and_is_weekends = list(zip(temps, is_weekends))

random_ages = list(map(lambda num: randint(25,65), range(0, 150)))

temps_weekends_and_ages = list(zip(temps, is_weekends, random_ages))


customers = list(map(lambda temps_and_is_weekend: 3*temps_and_is_weekend[0] + 40*temps_and_is_weekend[1] + 10, temps_and_is_weekends))
random_errors = list(map(lambda num: randint(-40,40), range(0, 150)))
customers_with_errors = list(map(lambda idx: customers[idx] + random_errors[idx],range(0, 150)))