import os


class File:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        if not os.path.exists(self.file_name):
            file = open(self.file_name, 'w')
            file.close()
        file = open(self.file_name, self.mode)
        return file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is (FileExistsError, FileNotFoundError):
            return True
        file.close()


with File('example.txt', 'w') as file:
    file.write('Всем привет!')