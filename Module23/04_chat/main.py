

def do_choice():
    try:
        print('Что хотите?:\n'
              '1) Посмотреть текущий текст чата\n'
              '2) Отправить сообщение')
        choice = int(input())
        if choice != 1 and choice != 2:
            raise BaseException
    except BaseException:
        print("Неверный ввод! Давай еще раз")
        return do_choice()
    return choice


def show_history():
    with open('file_log.txt','r') as file_log:
        print('Чат:\n' + file_log.read())


def send_message(user_name):
    message = input('Введите сообщение: ')
    with open('file_log.txt', 'a') as file_log:
        file_log.write(f'{user_name}: {message}\n')



def main(user_name):
    #show_history()
    choice = do_choice()
    if choice == 1:
        show_history()
    elif choice == 2:
        send_message(user_name)
    main(user_name)



user_name = input('Введите имя пользователя: ')
file_log = open('file_log.txt','w')

main(user_name)



