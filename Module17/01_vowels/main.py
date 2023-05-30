vowels = 'аяуюоеёэиыАЯУЮОЕЁЭИЫ'
text = str(input('Введите текст: '))
print()

ansver = [symbol for symbol in text if symbol in vowels]
print(ansver)
