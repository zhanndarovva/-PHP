# Вариант 16

# Пример 1
import numpy as n

A = n.array([3, -2, 5, 0, -1, 7, -8, 4, -6, 2])

positive_elements = A[A > 0]

squared = positive_elements ** 2

average = squared.mean()

print("Положительные элементы:", positive_elements)
print("Их квадраты:", squared)
print("Среднее арифметическое квадратов:", average)

# Пример 2
A = n.array([
    [1, 6, 3, 8],
    [5, 2, 9, 4],
    [7, 0, 5, 3],
    [6, 1, 2, 7]
])

less_than_5 = A[A < 5]

sum_less_than_5 = less_than_5.sum()

print("Элементы меньше 5:", less_than_5)
print("Сумма элементов меньше 5:", sum_less_than_5)