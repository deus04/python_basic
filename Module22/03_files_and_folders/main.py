import os


def count_and_getsize(any_path, count_dirs, count_files, total_size):
    for i_elem in os.listdir(any_path):
        full_path = os.path.join(any_path, i_elem)
        print(full_path)
        if os.path.isdir(full_path):
            count_dirs += 1
            count_dirs, count_files, total_size = count_and_getsize(full_path, count_dirs, count_files, total_size)
        elif os.path.isfile(full_path):
            count_files += 1
            total_size += os.path.getsize(full_path)

    return count_dirs, count_files, total_size


any_path = os.path.abspath(os.path.join('..', '..'))
print(any_path)
count_dirs = 0
count_files = 0
total_size = 0
count_dirs, count_files, total_size = count_and_getsize(any_path, count_dirs, count_files, total_size)
print('Размер каталога (в Кб):', total_size / 1024)
print('Количество подкаталогов:', count_dirs)
print('Количество файлов:', count_files)
