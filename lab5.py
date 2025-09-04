# Пример 1
lst = [1, 2, 3, 4, 5]
reversed_list = lst[::-1]

print("Обратный порядок:", reversed_list)
 
# Пример 2  
def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

numbers = [3, -10, 2, -7, 5]
print("Сортировка по убыванию абсолютного значения:", list_sort(numbers))
 
# Пример 3   
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

numbers = [10, 20, 30, 40, 50]
print("После замены:", change(numbers))