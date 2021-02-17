"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
with open('ex_5_2.txt') as in_file:
    cnt = 0
    cnt_wrds = []
    for line in in_file:
        cnt += 1
        wrds = line.split()
        cnt_wrds.append(len(wrds))
    print('Количество строк:', cnt)
    for j in range(len(cnt_wrds)):
        print(f'Количество слов в {j + 1} строке: {cnt_wrds[j]} ')
