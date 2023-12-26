import os


input_file_path = os.path.abspath(os.path.join('data', 'work_logs.txt'))
output_file_path = os.path.abspath(os.path.join('data',  'output_file.txt'))


def error_log_generator(input_file_path):
    if os.path.isfile(input_file_path):
        with open(input_file_path, 'r') as file:
            for i_line in file:
                if i_line.startswith('ERROR: '):
                    yield i_line
    else:
        raise FileNotFoundError("Файл не найден")


with open(output_file_path, 'w') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")
