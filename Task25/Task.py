# Задача 25. Напишите программу, которая принимает на вход строку, и отслеживает количество повторов каждого символа.

any_string = input('Введите что-нибудь ')

our_dictionary = {}

for i in any_string:
	if i in our_dictionary:                              # Ищем есть ли элемент в списке
		our_dictionary[i] = our_dictionary[i] + 1    # Если есть, добавляем + 1 к ключу
	else:
		our_dictionary[i] = 1			     # Ставим ключ к этому элементу в словаре 1

print(our_dictionary)

