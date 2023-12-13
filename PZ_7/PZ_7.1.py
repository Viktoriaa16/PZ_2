# 24 вариант
# Дана строка, состоящая из русских слов, набранных заглавными буквами и разделённых пробелами
# ( одним или несколькими). Найти количество слов, которые содержат ровно три буквы «А»
def count_words_with_three_A(input_string):
    words = input_string.split()
    count = 0

    for word in words:
        if word.count('А') == 3:
            count += 1
    return count


# пример использования функции
input_string = "ААА БББ АААААА"
print(count_words_with_three_A(input_string))