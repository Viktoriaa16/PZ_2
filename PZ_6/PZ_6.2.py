# 24 вариант
# Дан целочисленный список A размера N .
# Переписать в новый целочисленный список B того же размера вначале все элементы исходного списка с чётными номерами
# , а затем - с нечётными : A2, A4,....., A1, A3, A5,.......  . Условный оператор не использовать
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = A[1::2] + A[0::2]

print(B)