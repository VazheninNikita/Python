"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

with open('ex_5_7_in.txt') as in_file:
    firm_dict = {}
    tmp_list = []
    tmp_sum = 0
    tmp_count = 0

    for i in in_file:
        tmp_list.append(i.split())

    for j in tmp_list:
        tmp_profit = int(j[2]) - int(j[3])
        firm_dict.update({j[0]: tmp_profit})
        if tmp_profit >= 0:
            tmp_sum += tmp_profit
            tmp_count += 1
        profit_dict = {"average_profit": tmp_sum / tmp_count}

    out_lst = [firm_dict, profit_dict]
    print(out_lst)

with open('ex_5_7_out.json', 'w') as out_file:
    json.dump(out_lst, out_file)
