with open('text_file18-24.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    content_length = len(content)
    letter_count = sum(1 for char in content if char.isalpha())

    print("Содержимое файла:")
    print(content)
    print(f"Общее количество символов: {content_length}")
    print(f"Количество букв: {letter_count}")
    poem = content.upper()
    with open('poem_file.txt', 'w', encoding='utf-8') as poem_file:
        poem_file.write(poem)
        print("Текст стихотворения:")
        print(poem)
        print("Строки стихотворения записаны в файл poem_file.txt")