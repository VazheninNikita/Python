a = float(input('Укажите сколько км спортсмен пробежал в 1-й день: '))
b = float(input('Укажите сколько км нужно пробежать: '))
c = 1

if a < b:
    while a < b:
        a *= 1.1
        c += 1
    print(f'на {c}-й день спортсмен достиг результата — не менее {b} км')
else:
    print('Цель уже достигнута')
