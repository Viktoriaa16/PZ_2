# 24 вариант
# Составить список, в который будут включены только согласные буквы и
# привести их к верхнему регистру. Список:
# ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']

# Заданный список
words = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']

vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
consonants_list = []

for word in words:
    consonants_word = ''.join([letter.upper() for letter in word if letter.isalpha() and letter not in vowels])
    consonants_list.append(consonants_word)

print(consonants_list)
