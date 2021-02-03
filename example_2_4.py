my_list = input('Введите строку: ').split()

for i in range(len(my_list)):
    print(i, my_list[i][:10])
