# EASY
# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def func_for_name_age_city(name, age, city):
    print('{}, {} год(а), проживает в городе {}'.format(name, age, city))


func_for_name_age_city('Андрей', '28', 'Москва')


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_from_num(x, y, z):
    answer = max(x, y, z)
    return answer


result = max_from_num(2, 5, -6)
print(result)


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_list_of_args(*args):
    print(max(args, key=len))


max_list_of_args('aaaa', 'bbbbb', 'ccc', 'ffffff')

# MEDIUM
# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# # столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
names = ['Alex', 'Ivan', 'Viktor', 'Pavel', 'Grisha']
salary = [50000, 120000, 75000, 500000, 600000]
slovar = dict(zip(names, salary))
print(slovar.items())

with open('salary.txt', 'w', encoding='utf-8') as file:
    for k, v in slovar.items():
        file.write('{} - {}\n'.format(k, v))

file = open('salary.txt', 'r', encoding='utf-8')

new_names = []
new_salary = []
for line in file:
    x = float(line.split(' - ')[1]) * 0.87
    new_salary.append(x / 0.87)
    y = line.split(' - ')[0]
    new_names.append(y)
    print((line.split(' - ')[0]).upper(), x)  # решение с учетом вычета налога
print(list(
    zip(new_names, list(filter(lambda i: i < 500000, new_salary)))))  # решение с условием выводить только salary<500000
file.close()

# HARD
# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

import random

player = {'name': input(), 'health': 100, 'damage': random.randrange(1, 20)}
enemy = {'name': input(), 'health': 100, 'damage': random.randrange(1, 20)}


def attack(attacking, protecting):
    protecting['health'] = protecting['health'] - attacking['damage']
    return protecting['health']


print(player['name'], player['health'], enemy['name'], attack(player, enemy))

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import random

print('Введите имя первого Игрока: ')
player = {'name': input(), 'health': 100, 'damage': random.randrange(1, 20), 'armor': 1.2}
print('Введите имя второго Игрока: ')
enemy = {'name': input(), 'health': 100, 'damage': random.randrange(1, 20), 'armor': 1.2}


def attack(attacking):
    attack = attacking['damage']
    return attack


def damage(attack, protecting):
    damage = attack / protecting['armor']
    protecting['health'] = protecting['health'] - damage
    return damage


def game(play1, play2):
    while (play2['health']) > 0 and (play1['health']) > 0:
        d1 = damage(attack(play1), play2)
        d2 = damage(attack(play2), play1)
    else:
        print('Конец поединка')
        if play2['health'] > play1['health']:
            print('Победил: ', play2['name'])
        else:
            print('Победил: ', play1['name'])

    print(play1, '\n', play2)

    return play1, play2


game(player, enemy)
