# Задача на собеседовании №1.
# Создайте список из случайных чисел. Найдите номер его последнего локального максимума 
# (локальный максимум - это элемент, который больше любого из своих соседей).

import random

new_list = [random.randint(1, 100) for _ in range(10)]
print(new_list)

for i in range(len(new_list) - 2, 0, -1):
	if new_list[i - 1] < new_list[i] > new_list[i + 1]:
		print(i)
		print(new_list[i])
		break