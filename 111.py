import os


def acceptCommand():
    '''
    :return: Requests the command number and if the command number is specified incorrectly, displays an error message.
    Commands are requested until the correct command number is entered. Returns the correct command number.
    '''
    q = False
    while q != True:
        num = input('Выберите пункт меню: ')
        try:
            num = int(num)
            if num <= 7 and num >= 1:
                a = True
            else:
                a = False
            if a == False:
                print('Номер введен ошибочно. Повторите попытку.')
                num = int(input('Выберите пункт меню: '))
        except ValueError:
            print('Введенное "{}" не является числом. Повторите попытку.'.format(num))
        else:
            q = True
    if num == 7:
        return 'QUIK'
    return num


def moveDown(currentDir):
    '''
    :param currentDir: directory to be parent
    :return: Requests the name of a subdirectory. If the name is specified correctly,
    it makes the directory in currentDir current, otherwise it displays an error message.
    '''
    a = False
    while a != True:
        name = input('Введите имя папки, в которую хотите переместиться, или файла, который хотите открыть: ')
        new_path = os.path.join(currentDir, name)
        if os.path.exists(new_path) == True:
            a = True
        else:
            print('Папка\файл не существует. Повторите попытку.')
            a = False
    if os.path.isdir(new_path) == True:
        return os.chdir(new_path)
    if os.path.isfile(new_path) == True:
        return os.startfile(new_path)


def moveUp():
    '''
    :return: Makes the parent directory current.
    '''
    path = os.getcwd()
    new_path = os.path.dirname(path)  # parent
    os.chdir(new_path)


def findFiles(path, target, new_path):
    '''
    :param path: The directory in which the required file is searched.
    :param target: The name of the file to find the path to.
    :param new_path: Parent directory.
    :return: A recursive function that generates a list of paths to files that contain target.
    If the files are not found, displays a corresponding message.
    '''
    if os.path.isfile(target) == True:
        spisok2 = []
        spisok = os.listdir(path)
        if len(spisok) != 0:
            for i in spisok:
                if os.path.isfile(i) == True and i == target:
                    print(os.path.join(path, i))
                spisok2.append(i)
            return findFiles(os.path.join(path, i), target, new_path)
        return ''
    print()
    print('Данный файл не найден.')
    return ''


def countFiles(path):
    '''
    :param path: Used directory.
    :return: A recursive function that counts the number of files in the specified path.
    All files in subdirectories are included in the count. Returns the number of files.
    '''
    if os.path.isfile(path):
        return 1

    count = 0
    dir_list = os.listdir(path)
    for d in dir_list:
        new_path = path + '\\' + d
        count += countFiles(new_path)

    return count


def countDirs(path):
    count = 0
    dir_list = os.listdir(path)
    for d in dir_list:
        new_path = path + '\\' + d
        if os.path.isdir(new_path):
            count += 1
            count += countDirs(new_path)
    return count


def countBytes(path):
    '''
    :param path: Used directory.
    :return: A recursive function that calculates the total size (in bytes) of all files in the specified path.
    All files in subdirectories are included in the count. Returns the total number of bytes.
    '''
    if os.path.isfile(path):
        return os.path.getsize(path)

    count = 0
    dir_list = os.listdir(path)
    for d in dir_list:
        new_path = path + '\\' + d
        count += countBytes(new_path)

    return count


def runCommand(command):
    '''
    :param command: Command number from the menu list.
    :return: Determines by the number of the command command which function should be executed.
    '''
    if command == 1:
        print()
        dir = []
        files = []
        path = os.getcwd()
        for item in os.scandir(path):
            if item.is_dir():
                dir.append(item.name)
            if item.is_file():
                files.append(item.name)
        print('Папки: ', *dir)
        print('Файлы: ', *files)
        print()

    if command == 2:
        print()
        moveUp()
        print()

    if command == 3:
        print()
        path = os.getcwd()
        moveDown(path)
        print()

    if command == 4:
        print()
        path = os.getcwd()
        print('Количество файлов:', countFiles(path))
        print('Количество папок:', countDirs(path))
        print()

    if command == 5:
        print()
        path = os.getcwd()
        print('Размер текущего каталога (в байтах): ', countBytes(path))
        print()

    if command == 6:
        print()
        path = os.getcwd()
        target = input('Введите файл, который хотите найти, с расширением: ')
        new_path = path
        print()
        print(findFiles(path, target, new_path))
        print()


def main():
    '''
    :return: The main program that prints the path to the current directory and menu.
    Causes the execution of a command function.
    '''
    while True:
        print(os.getcwd())
        print('', 'Меню:', '1. Просмотр каталога', '2. На уровень вверх', '3. На уровень аниз',
              '4. Количесвто файлов и каталогов',
              '5. Размер текущего каталога (в байтах)', '6. Поиск файла', '7. Выход из программы', '', sep='\n')
        command = acceptCommand()
        if command == 'QUIK':
            print()
            print('Работа программы завершена.')
            break
        print()
        runCommand(command)


main()