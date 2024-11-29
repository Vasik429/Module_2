def get_matrix (n, m, value): # создать функцию
    matrix = [] # создать список внутри функции
    for i in range (n): # cоздать внеш цикл
        result1 = []
        result2 = []
        result3 = []
        matrix.append(result1)
        for j in range (m):
            result1.append(value)
            result2.append(value)
            result3.append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)