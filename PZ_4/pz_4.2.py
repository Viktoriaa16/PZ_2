# Даны целые положительные числа N и К.
# Используя только операции сложения и вычитания, найти частное от деления нацело N на K,
# также остаток от этого деления
def divide(N, K):
    quotient = 0  # частное от деления
    remainder = N  # остаток от деления

    while remainder >= K: # для вычитания  K из  remainder  увеличения quotient на 1, пока Remainder больше или равен 1
        quotient += 1
        remainder -= K

    return quotient, remainder  # возвр найденное число


N = int(input("Введите число "))
K = int(input("Введите число "))

q, r = divide(N, K)
print("Частное: ", q)
print("Остаток: ", r)