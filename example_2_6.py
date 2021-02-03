goods = []
i = 1
question = 'y'
an_dict = {'название': [], 'цена': [], 'количество': [], 'eд': []}

while question == 'y':
    my_dict = {}
    my_dict['название'] = input('Название товара: ')
    my_dict['цена'] = float(input('Цена: '))
    my_dict['количество'] = int(input('Количество: '))
    my_dict['eд'] = input('Единица измерения: ')
    my_tuple = (i, my_dict)
    goods.append(my_tuple)
    i += 1
    question = input('Хотите добавить еще товар? (y/n) ')

print(goods)
print()

for i in range(len(goods)):
    for key, value in goods[i][1].items():
        for k, v in an_dict.items():
            if key == k:
                an_dict[k] += [value]
print(an_dict)
'''
В примере “ед”: [“шт.”] не повторяются, но при этом значения словаря просят сделать списком, не множеством. 
Считаю, корректнее повторять значения, так как единицы могут быть не только одного наименования и может возникнуть 
путаница, в случае их чередования.
'''
