import os

def count_and_getsize(any_path, count_dirs, count_files, total_size):
    for i_elem in os.listdir(any_path):
        i_elem = os.path.join(any_path, i_elem) # FIXME мне не нравится это переприсваивание. Это верно?
        print(i_elem)
        if os.path.isdir(i_elem):
            count_dirs += 1
            count_and_getsize(i_elem, count_dirs, count_files, total_size)
        elif os.path.isfile(i_elem):
            count_files += 1
            total_size += os.path.getsize(i_elem)

    return count_dirs, count_files, total_size


#any_path = os.path.abspath(os.path.join('..','..')) # TODO с Этим путем не работает
any_path = os.path.abspath('..')                    # TODO а с этим работает. Почему?
print(any_path)
count_dirs = 0
count_files = 0
total_size = 0
count_dirs, count_files, total_size = count_and_getsize(any_path, count_dirs, count_files, total_size)
print('Размер каталога (в Кб):', total_size/1024)
print('Количество подкаталогов:', count_dirs)
print('Количество файлов:', count_files)

