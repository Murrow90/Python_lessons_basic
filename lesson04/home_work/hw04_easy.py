# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
list1 = []
list2 = []

list1 = [random.randint(1, 10) for _ in range(10)]
list2 = [el ** 2 for el in list1]

print(list1)
print(list2)



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list1 = ["пэрсик", "инжир свежий","инжир несвежий", "айва", "опунция"]
list2 = ["опунция", "билимби", "грейпфрут", "инжир несвежий", "жаботикаба"]
# список фруктов взят с Википедии #
list_new = []

list_new = [el for el in list1 if el in list2]
print(list_new)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


import random

list1 = []
list2 = []
list3 = []
list4 = []

list1 = [random.randint(-20, 20) for _ in range(20)]
list2 = [el for el in list1 if el % 3 == 0]
list3 = [el for el in list1 if el > 0]
list4 = [el for el in list1 if el % 4 != 0]

new_list = []
final_list = []

new_list = [el for el in list3 if el in list2]
final_list = [el for el in new_list if el in list4]


print(final_list)
