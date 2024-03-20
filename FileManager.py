import os
import shutil


class FileManager:
    def __init__(self, working_directory):
        self.working_directory = working_directory

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.working_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.working_directory, folder_name)
        shutil.rmtree(folder_path)

    def move_to_folder(self, folder_name):
        if folder_name == '..':
            self.working_directory = os.path.dirname(self.working_directory)
        else:
            new_directory = os.path.join(self.working_directory, folder_name)
            if os.path.isdir(new_directory):
                self.working_directory = new_directory
            else:
                print('Папка не существует')

    def create_file(self, file_name):
        file_path = os.path.join(self.working_directory, file_name)
        open(file_path, 'a').close()

    def write_to_file(self, file_name, text):
        file_path = os.path.join(self.working_directory, file_name)
        with open(file_path, 'w') as file:
            file.write(text)

    def view_file(self, file_name):
        file_path = os.path.join(self.working_directory, file_name)
        with open(file_path, 'r') as file:
            print(file.read())

    def delete_file(self, file_name):
        file_path = os.path.join(self.working_directory, file_name)
        os.remove(file_path)

    def copy_file(self, source_file, destination_folder):
        source_path = os.path.join(self.working_directory, source_file)
        destination_path = os.path.join(self.working_directory, destination_folder, source_file)
        shutil.copyfile(source_path, destination_path)

    def move_file(self, source_file, destination_folder):
        source_path = os.path.join(self.working_directory, source_file)
        destination_path = os.path.join(self.working_directory, destination_folder, source_file)
        shutil.move(source_path, destination_path)

    def rename_file(self, old_name, new_name):
        old_path = os.path.join(self.working_directory, old_name)
        new_path = os.path.join(self.working_directory, new_name)
        os.rename(old_path, new_path)

    def list_current_directory(self):
        contents = os.listdir(self.working_directory)
        print("Содержание текущей папки:")
        for item in contents:
            print(item)
        print()
