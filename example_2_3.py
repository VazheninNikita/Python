# Решение через список
mnth_l = 0

while mnth_l < 1 or mnth_l > 12:
    mnth_l = int(input('Введите номер месяца: '))

ssns_l = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

print(ssns_l[mnth_l - 1])

# Решение через словарь
mnth_d = 0

while mnth_d < 1 or mnth_d > 12:
    mnth_d = int(input('Введите номер месяца: '))

ssns_d = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
          10: 'осень', 11: 'осень', 12: 'зима'}

print(ssns_d[mnth_d])

# Решение через словарь списков
mnth_dl = 0

while mnth_dl < 1 or mnth_dl > 12:
    mnth_dl = int(input('Введите номер месяца: '))

ssns_dl = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for key, value in ssns_dl.items():
    if mnth_dl in value:
        print(key)
