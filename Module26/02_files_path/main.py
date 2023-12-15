import os


def gen_files_path(dir_name):
    any_path = os.path.join('M:\\')  # TODO как правильно выводить "\" ? тригерится если только 1 "\"
    print(any_path)
    # any_path = os.path.abspath(os.path.join('..', '..'))
    for address, dirs, files in os.walk(any_path):
        if dir_name in dirs:
            for name in dirs:
                if name == dir_name:
                    for file in os.listdir(os.path.join(address, name)):
                        yield os.path.join(address, name, file)

# TODO какаято очень сложная для меня тема с модулем path. я прям теряюсь


dir_name = '02_files_path'
#dir_name = 'test.txt'
gen = gen_files_path(dir_name)
for i_path in gen:
    print(i_path)