# создаем переменную, равную 1
# var = 1
# прописываем цикл с условием - выполнять до тех пор, пока переменная
# меньше или равна 13
# while var <= 13:
    # выводим значение переменной
    # print(var)
    # увеличиваем переменную на 1
    # var += 1

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
#     print(i)

# for i in range(1, 14):
#     print(i, end=' ')

# for var in 'Python':
#     if var == 'h':
#         continue
#     print(var)

# for var in 'Python':
#     if var == 'h':
#         break
#     print(var)

for var in 'Python':
    if var == 'a':
        break
else:
    print('Символа a нет в слове Python')
