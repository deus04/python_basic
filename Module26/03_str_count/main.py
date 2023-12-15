import os


def line_counting():
    # path = 'M:\GitLab\Skillbox\python_basic\Module26\03_str_count'
    for i_file in os.listdir():
        if str(i_file).endswith('.py'):
            count = 0
            with open(i_file, 'r') as file:
                for i_line in file:
                    if not (i_line.startswith('\n') or i_line.startswith('#')):
                        count += 1
            yield i_file, count


counter = line_counting()
for i_file, count in counter:
    print('File name: {}    Count: {}'.format(i_file, count))