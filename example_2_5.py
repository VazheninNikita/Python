my_list = [7, 5, 3, 3, 2]

el = int(input('Введите значение: '))

if el not in my_list:
    my_list.append(el)
    my_list.sort(reverse=True)
else:
    my_list.insert(my_list.index(el) + my_list.count(el), el)  # по условию нужно поместить после существующих значений

print(my_list)
