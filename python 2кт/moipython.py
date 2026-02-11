#1
# a = [1,2,3,4,5,6,7,8,9,10]

# print(a)

# a.reverse()

# print(a)

#2
# import random

# rows = int(input("Введите количество строк: "))
# cols = int(input("Введите количество столбцов: "))

# matrix = []

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(random.randint(-20, 20))
#     matrix.append(row)

# print("Матрица:")
# for row in matrix:
#     print(row)

# min_element = min(min(row) for row in matrix)
# print("Минимальный элемент:", min_element)

# if rows >= 2:
#     print("Вторая строка:", matrix[1])
# else:
#     print("Второй строки нет")

# print("Первый столбец:")
# for i in range(rows):
#     print(matrix[i][0])

#3
# n = 5  
# arr = []

# print("Введите элементы массива:")
# for i in range(n):
#     arr.append(int(input()))

# found = False

# for i in range(len(arr) - 1):
#     if arr[i] == 0 and arr[i + 1] == 0:
#         found = True
#         break

# if found:
#     print("В массиве есть два подряд идущих нуля")
# else:
#     print("Двух подряд идущих нулей нет")

#4
# import random

# n = 10
# arr = []

# for i in range(n):
#     arr.append(random.randint(1, 50))

# print("Массив:", arr)

# count_div3 = 0
# for num in arr:
#     if num % 3 == 0:
#         count_div3 += 1

# print("Количество чисел, делящихся на 3:", count_div3)

# sum_even = 0
# count_even = 0

# for num in arr:
#     if num % 2 == 0:
#         sum_even += num
#         count_even += 1

# if count_even > 0:
#     print("Среднее чётных чисел:", sum_even / count_even)
# else:
#     print("Чётных чисел нет")