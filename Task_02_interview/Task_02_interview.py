# Задача на собеседовании №2.
# Создайте список из случайных чисел. Найдите второй максимум.

new_list = list(set([10, 10, 8, 9, 3, 4, 5]))
print(new_list)

first_max, second_max = new_list[0], new_list[1]

for i in new_list:
	if i > first_max:
		second_max = first_max
		first_max = i
	elif i > second_max and i != first_max:
		second_max = i

print(second_max)