# 24 вариант
# Даны строки S, S1 и S2. Заменить в строке S первое вхождение строки S1 на строку S2
def replace_first_occurrence(S, S1, S2):
    index = S.find(S1)
    if index != -1:
        new_S = S[:index] + S2 + S[index + len(S1):]
        return new_S
    else:
        return S

# пример использования функции
S = "abcabcacc"
S1 = "bc"
S2 = "xy"
print(replace_first_occurrence(S, S1, S2))
