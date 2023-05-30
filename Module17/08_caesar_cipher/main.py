def cipher(message, shift):
    new_message = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in message]
    answer = ''
    for i_word in new_message:
        answer += i_word
    return answer


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = str(input('Введите сообщение: '))
shift = int(input('Введите сдвиг: '))

answer = cipher(message, shift)
print('Зашифрованное сообщение:', answer)
