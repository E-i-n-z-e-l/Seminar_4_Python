# Задача 27. Задача №27. Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов содержится в этом тексте.
# Пример:

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 13


our_test = input('Введите текст ') + ' '      # Вводим на конце пробел чтобы алгоритм наш работал (цикл for)

word_set = set()

word = ''

for i in our_test:
	if i != ' ':
		word = word + i
	else:
		word_set.add(word)	     # С помощью команды 'set' добавляем слово к нашему множеству
		word = ''

print(len(word_set))			     # С помощью команды 'len' узнаем длину множетства