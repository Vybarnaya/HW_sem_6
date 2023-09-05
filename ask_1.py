# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random

def get_array(a):
    list1 = []
    for i in range(a):
        list1.append(random.randint(1,20))
    return list1

def arr_ind(arr,ran):
    list2 = []
    for i in range(0,len(arr)):
        if arr[i] in ran:
            list2.append(i)
    return list2


n = int(input('введите количество элементов массива:'))
d = range(3,10+1)

list3 = get_array(n)
list4 = arr_ind(list3,d)

print(list3)
print(list4)



