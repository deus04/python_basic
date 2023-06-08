def exam_ip(ip_address):
    digits = '1234567890'
    split_numbers = ip_address.split('.')

    if len(split_numbers) != 4:
        return print('Адрес — это четыре числа, разделённые точками.')

    for number in split_numbers:
        for symbol in number:
            if not symbol in digits:
                return print(number, '— это не целое число')
        if int(number) > 255:
            return print(number,'превышает 255')
    return print('IP-адрес корректен.')



ip_address = input('Введите IP: ')

exam_ip(ip_address)

