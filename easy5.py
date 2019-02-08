import os, sys


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
