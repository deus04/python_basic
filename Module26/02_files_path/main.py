import os


def gen_files_path(dir_name):
    any_path = os.path.join('M:/')
    print(any_path)
    for address, dirs, files in os.walk(any_path):
        if address.endswith(dir_name):
            for file in files:
                yield os.path.join(address, dir_name, file)


dir_name = '02_files_path'
gen = gen_files_path(dir_name)
for i_path in gen:
    print(i_path)