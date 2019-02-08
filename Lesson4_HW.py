# EASY
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list = [1, 2, 4, 0, -2, -8]
list_new = [i ** 2 for i in list]
print(list_new)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_1 = ['яблоко', 'ананас', 'киви', 'апельсин', 'вишня']
list_2 = ['яблоко', 'слива', 'киви', 'манго', 'вишня']

list_3 = [k for k in list_1 for v in list_2 if k == v]
print(list_3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list_4 = [1, 2, 4, 0, -2, 9]
list_5 = [i for i in list_4 if i % 3 == 0 and i > 0 and (i % 4) == 1]
print(list_5)

# MEDIUM
# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
email = input('Введите email: ')
pattern_email = '([a-z+\_0-9]+)@([a-z_0-9]+)\.(ru|com|org)'
pattern_letter = '^[A-Z]\w+'
result_name = re.search(pattern_letter, name)
result_surname = re.search(pattern_letter, surname)
result_email = re.search(pattern_email, email)
if result_surname == None and result_name == None:
    print(surname, name, '-неверно указана фамилия и имя')
elif result_surname == None:
    print(surname, name, '-неверно указана фамилия')
elif result_name == None:
    print(surname, name, '-неверно указано имя')
else:
    print(surname, name)
print('Неправильно указан email' if result_email == None else email)

# Задача - 2:
# Вам дан текст:
import re

some_str = 'Мороз и солнце; день чудесный!\
Еще ты дремлешь, друг прелестный —\
Пора, красавица, проснись:\
Открой сомкнуты негой взоры\
Навстречу северной Авроры,\
Звездою севера явись!\
Вечор, ты помнишь, вьюга злилась,\
На мутном небе мгла носилась;\
Луна, как бледное пятно,\
Сквозь тучи мрачные желтела,\
И ты печальная сидела —\
А нынче... погляди в окно:\
Под голубыми небесами\
Великолепными коврами,\
Блестя на солнце, снег лежит;\
Прозрачный лес один чернеет,\
И ель сквозь иней зеленеет,\
И речка подо льдом блестит.\
Вся комната янтарным блеском\
Озарена. Веселым треском\
Трещит затопленная печь.\
Приятно думать у лежанки.\
Но знаешь: не велеть ли в санки\
Кобылку бурую запречь?\
Скользя по утреннему снегу,\
Друг милый, предадимся бегу\
Нетерпеливого коня\
И навестим поля пустые,\
Леса, недавно столь густые,\
И берег, милый для меня.'

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

# some_str = 'text.asdf.asd.asdf.afasdf.kjsfk.'
pattern = '\.+\.'
print(some_str if re.search(pattern, some_str) == None else str(some_str) + '\nВ тексте есть подряд больше одной точни')
