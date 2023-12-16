import os


def gen_files_path(dir_name):
    any_path = os.path.join('M:\\')  #  как правильно выводить "\" ? тригерится если только 1 "\"
                                     # TODO Более универсально использовать одну "прямую" вместо двух "обратных" косых
                                     #  черт, так не толькно под Windows, но и под Linux работает
    print(any_path)
    # any_path = os.path.abspath(os.path.join('..', '..'))
    for address, dirs, files in os.walk(any_path):
        if dir_name in dirs:
            for name in dirs:
                if name == dir_name:
                    for file in os.listdir(os.path.join(address, name)):
                        # TODO лишний цикл, walk выдаёт полный список всех папок и файлов, в том числе вложенных
                        yield os.path.join(address, name, file)

#  какаято очень сложная для меня тема с модулем path. я прям теряюсь
# TODO Это у всех так, кто с файловой системой ещё не работал, больше практики


dir_name = '02_files_path'
#dir_name = 'test.txt'
gen = gen_files_path(dir_name)
for i_path in gen:
    print(i_path)