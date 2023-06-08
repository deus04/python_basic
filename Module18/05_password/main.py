def exam_password():
    numbers = '1234567890'
    password = input('Придумайте пароль: ')
    number_count = 0
    upper_count = 0

    for symbol in password:
        if symbol in numbers:
            number_count += 1
        elif symbol == symbol.upper():
            upper_count += 1
    if (len(password) < 8) or (number_count < 3) or (upper_count < 1):
        print('Пароль ненадежный. Попробуйте еще раз')
        exam_password()
    else:
        print('Это надёжный пароль!')


exam_password()
