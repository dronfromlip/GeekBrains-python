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

print('sys.argv = ', sys.argv)


def help():
    print(
        '****Меню*****\n\n 1. Перейти в папку \n 2. Просмотреть содержимое текущей папки\n 3. Удалить папку\n 4. Создать папку \n Q. Выход\n')


def go_to_folder():
    print('1. Перейти в папку \n')
    folder_name = input('Введите путь к папке для просмотра: ')

    if folder_name == 'GeekBrains-python.git':
        folder_name = sys.path[0]

    try:
        os.chdir(folder_name)
        print('Вы перешли в папку: {}'.format(folder_name))
        # for i in os.listdir(os.getcwd()):
        #     print(i)
    except Exception as e:
        print('Такой папки нет или имя введено неправильно')
    path = os.getcwd()
    return path


def view_current_folder():
    print('2. Просмотреть содержимое текущей папки\n')
    print('Вы находитесь здесь: ', os.getcwd())
    for i in os.listdir(os.getcwd()):
        print(i)


def delete_folder():
    print('3. Удалить папку\n')
    folder_name = input('Введите название папки для удаления: ')
    try:
        os.rmdir(folder_name)
        print('Папка: {} удалена'.format(folder_name))
    except FileNotFoundError:
        print('Такая папка не существует. Удалить невозможно')
        return


def new_folder():
    print('4. Создать папку\n')
    folder_name = input('Введите название папки: ')

    if not folder_name:
        print("Необходимо указать имя папки ")
        return
    dir_path = os.path.join(os.getcwd(), folder_name)
    try:
        os.mkdir(dir_path)
        print('Папка: {} создана'.format(folder_name))
    except FileExistsError:
        print('Такая папка уже существует. Попробуйте еще раз')
        return


do = {
    'help': help,
    '1': go_to_folder,
    '2': view_current_folder,
    '3': delete_folder,
    '4': new_folder
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
