#1
# print("1. Сколько будет 2 + 2?")
# print("1 3")
# print("2 4")
# print("3 5")
# a = int(input())
# if a == 2:
#     print("Правильно")
# else:
#     print("Не правильно")


# print("2. Столица России?")
# print("1 Москва")
# print("2 Париж")
# print("3 Берлин")
# a = int(input())
# if a == 1:
#     print("Правильно")
# else:
#     print("Не правильно")


# print("3. Сколько дней в неделе?")
# print("1 5")
# print("2 6")
# print("3 7")
# a = int(input())
# if a == 3:
#     print("Правильно")
# else:
#     print("Не правильно")


# print("4. Какой сейчас век?")
# print("1 19")
# print("2 21")
# print("3 18")
# a = int(input())
# if a == 2:
#     print("Правильно")
# else:
#     print("Не правильно")


# print("5. Сколько месяцев в году?")
# print("1 10")
# print("2 11")
# print("3 12")
# a = int(input())
# if a == 3:
#     print("Правильно")
# else:
#     print("Не правильно")


# print("6. Сколько сторон у квадрата?")
# print("1 3")
# print("2 4")
# print("3 5")
# a = int(input())
# if a == 2:
#     print("Правильно")
# else:
#     print("Не правильно")


# print("7. 5 * 2 =")
# print("1 7")
# print("2 10")
# print("3 12")
# a = int(input())
# if a == 2:
#     print("Правильно")
# else:
#     print("Не правильно")


# print("8. Какой язык мы изучаем?")
# print("1 Python")
# print("2 English")
# print("3 Math")
# a = int(input())
# if a == 1:
#     print("Правильно")
# else:
#     print("Не правильно")

# print("9. Сколько часов в сутках?")
# print("1 12")
# print("2 24")
# print("3 48")
# a = int(input())
# if a == 2:
#     print("Правильно")
# else:
#     print("Не правильно")

# print("10. Солнце это?")
# print("1 Планета")
# print("2 Звезда")
# print("3 Спутник")
# a = int(input())
# if a == 2:
#     print("Правильно")
# else:
#     print("Не правильно")

# #2
# import math

# a = float(input())
# b = float(input())
# c = float(input())

# D = b*b - 4*a*c

# if D > 0:
#     x1 = (-b + math.sqrt(D)) / (2*a)
#     x2 = (-b - math.sqrt(D)) / (2*a)
#     print(x1, x2)
# elif D == 0:
#     x = -b / (2*a)
#     print(x)
# else:
#     print("Нет корней")


# #3
# s = 0
# k = 0

# while True:
#     n = int(input())

#     if n % 2 == 0:
#         s = s + n
#         k = k + 1

#     if n == 100:
#         break

# print(s / k)

# #4
# words = input().split()
# ok = True

# for w in words:
#     if w[0] not in "ABCabc":
#         ok = False

# if ok:
#     print("YES")
# else:
#     print("NO")