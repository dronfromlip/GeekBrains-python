# EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

try:
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
        os.mkdir(dir_path)

except FileExistsError:
    print('Такая директория уже существует')

try:
    for i in range(1, 10):
        os.rmdir('dir_' + str(i))
except FileNotFoundError:
    print('Такая директория не существует')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print(next(os.walk('.'))[1])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os, sys
import shutil

try:
    shutil.copy(sys.argv[0], 'copy-{}'.format(sys.argv[0]))
except IOError:
    print ('Не удалось создать копию')

print (os.listdir("."))

# MEDIUM

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"
import os, sys
import easy5

print('sys.argv = ', sys.argv)


def help():
    print(
        '****Меню*****\n\n 1. Перейти в папку \n 2. Просмотреть содержимое текущей папки\n 3. Удалить папку\n 4. Создать папку \n Q. Выход\n')



do = {
    'help': help,
    '1': easy5.go_to_folder(),
    '2': easy5.view_current_folder(),
    '3': easy5.delete_folder(),
    '4': easy5.new_folder()
}

if __name__ == '__main__':
    try:
        arg_command = sys.argv[1]
    except IndexError:
        arg_command = ''
    Done = False
    while not Done:
        if arg_command == '':
            print(
                '\n****Меню*****\n\n 1. Перейти в папку \n 2. Просмотреть содержимое текущей папки\n 3. Удалить папку\n 4. Создать папку\n Q. Выход \n')
            key = input('Выберете пункт меню: ')
        else:
            key = arg_command
            arg_command = ''
        if key != ('Q' and ''):
            if do.get(key):
                do[key]()
            elif key == 'Q':
                break
            else:
                print('Задан неверный ключ')
                print('Укажите ключ help для получения справки')
