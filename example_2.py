m = int(input('Введите время в секундах: '))

d = m // 86400  # Количество дней
hh = str((m - d * 86400) // 3600).zfill(2)  # Часы
mm = str((m // 60) % 60).zfill(2)  # Минуты
ss = str(m % 60).zfill(2)  # Секунды

if d == 0:
    print(f'{hh}:{mm}:{ss}')
else:
    print(f'{d} дней {hh}:{mm}:{ss}')
