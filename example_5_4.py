"""
Создать (не программно) текстовый файл со следующим содержимым:

One — 1

Two — 2

Three — 3

Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
with open('ex_5_4_in.txt') as in_file:
    content_in = in_file.readlines()
    content_out = []
    for i in content_in:
        if i.find('One') > -1:
            content_out.append(i.replace('One', 'Один'))
        elif i.find('Two') > -1:
            content_out.append(i.replace('Two', 'Два'))
        elif i.find('Three') > -1:
            content_out.append(i.replace('Three', 'Три'))
        elif i.find('Four') > -1:
            content_out.append(i.replace('Four', 'Четыре'))
        else:
            content_out.append(i)

with open('ex_5_4_out.txt', 'w') as out_file:
    out_file.writelines(content_out)
