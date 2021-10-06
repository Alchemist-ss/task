import logging
from pathlib import Path


# Подсчёт строк для "Библии"
f_str0 = open('Библия.txt')
a = 0
for line in f_str0: # for - перебор элиментов
    a += 1 # цифра это длина шага
f_str0.close()
# Подсчёт слов для "Библии"
f_str0 = open('Библия.txt')
words0 = 0
for word in f_str0.read().split(): # .read - чтение файла целиком, .split() - разделитьель слов от пробелов
    words0 += 1
f_str0.close()
#

# Подсчёт строк для "Божественная комедия"
f_str1 = open('Божественная комедия.txt')
b = 0
for line in f_str1:
    b += 1
f_str1.close()
# Подсчёт слов в "Божественная комедия"
f_str1 = open('Божественная комедия.txt')
words1 = 0
for word in f_str1.read().split():
    words1 += 1
f_str1.close()

# Подсчёт строк для "Путь лидера"
f_str2 = open('Путь лидера.txt')
c = 0
for line in f_str2:
    c += 1
f_str2.close()
# Подсчёт слов в "Путль лидера"
f_str2 = open('Путь лидера.txt')
words2 = 0
for word in f_str2.read().split():
    words2 += 1
f_str2.close()

title = "Название файла: "
extension = "Расширение: "
# вывод расширения у каждого файла
ext0 = (Path ('Библия.txt').suffix)
ext1 = (Path ('Божественная комедия.txt').suffix)
ext2 = (Path ('Путь лидера.txt').suffix)
text_str = "Количество строк: "
word_count = "Количество слов: "
frequent_word = "Часто встречающееся слово: "
first_text = "Первое включение в текст: "

# Запись для внесения записей в наш файл
# Вписываю все знания о "Библии"
f = open('task.txt', 'w') # (w - writing(запись))
f.write(title + f_str0.name + "\n") # f.write записываю текст в файл
f.write(extension + ext0 + "\n")
f.write(text_str + str(a) + "\n")
f.write(word_count + str(words0) + "\n")
f.write(frequent_word + "\n")
f.write(first_text + "\n" + "\n")
with open('Библия.txt', 'r') as file:
    f.write(file.read() + "\n")

# Вписываю всё что есть в "Божественная комедия"
f.write(title + f_str1.name + "\n")
f.write(extension + ext1 + "\n")
f.write(text_str + str(b) + "\n")
f.write(word_count + str(words1) + "\n")
f.write(frequent_word + "\n")
f.write(first_text + "\n" + "\n")
with open('Божественная комедия.txt', 'r') as file:
    f.write(file.read() + "\n" + "\n")
# Вписываю в файл всё о "Пути лидера"

f.write(title + f_str2.name + "\n")
f.write(extension + ext2 + "\n")
f.write(text_str + str(c) + "\n")
f.write(word_count + str(words2) + "\n")
f.write(frequent_word + "\n")
f.write(first_text + "\n" + "\n")
with open('Путь лидера.txt', 'r') as file:
    f.write(file.read())
f.close() # закрытие файла

logging.basicConfig(level=logging.ERROR)
logging.error('Если я правильно понял то будут выводиться ошибки с уровнем ERROR')
