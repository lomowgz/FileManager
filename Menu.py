from FileManager import *


class Menu:
    def __init__(self, path):
        self.path = path
        self.file_manager = FileManager(path)
        self.working_dir = self.file_manager.working_directory

    def do_action(self, choice):
        if choice == 1:
            name = input('Введите название папки: ')
            self.file_manager.create_folder(name)
        elif choice == 2:
            name = input('Введите название папки: ')
            self.file_manager.delete_folder(name)
        elif choice == 3:
            name = input('Введите название папки: ')
            self.file_manager.move_to_folder(name)
            self.working_dir = self.file_manager.working_directory
        elif choice == 4:
            name = input('Введите название файла: ')
            self.file_manager.create_file(name)
        elif choice == 5:
            name = input('Введите название файла: ')
            text = input('Введите текст: ')
            self.file_manager.write_to_file(name, text)
        elif choice == 6:
            name = input('Введите название файла: ')
            self.file_manager.view_file(name)
        elif choice == 7:
            name = input('Введите название файла: ')
            self.file_manager.delete_file(name)
        elif choice == 8:
            name_1 = input('Введите название файла для копирования: ')
            name_2 = input('Введите название папки куда копировать: ')
            self.file_manager.copy_file(name_1, name_2)
        elif choice == 9:
            name_1 = input('Введите название файла для перемещения: ')
            name_2 = input('Введите название папки куда переместить: ')
            self.file_manager.move_file(name_1, name_2)
        elif choice == 10:
            name_1 = input('Введите название файла для переименования: ')
            name_2 = input('Введите новое название файла: ')
            self.file_manager.rename_file(name_1, name_2)
        elif choice == 11:
            self.file_manager.list_current_directory()

    def run(self):
        action = None

        while action != 0:
            print(f'1. Создать папку\n'
                  f'2. Удалить папку\n'
                  f'3. Переместиться в папку\n'
                  f'4. Создать файл\n'
                  f'5. Редактировать файл\n'
                  f'6. Вывести файл\n'
                  f'7. Удалить файл\n'
                  f'8. Скопировать файл\n'
                  f'9. Переместить файл\n'
                  f'10. Переименовать файл\n'
                  f'11. Посмотреть содержимое текущей папки\n'
                  f'0. Выход\n')

            action = int(input(f'Введите действие ({self.working_dir}/): '))
            self.do_action(action)
