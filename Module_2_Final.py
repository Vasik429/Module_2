import random

def Password (number):
    pass_ = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_

number = random.randint(3, 20)
result1 = Password(number)
print(number)
print(result1)


def Password (number):
    pass_ = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_
k = 0
while k < 5:
    print(Password(int(input('Введите число от 3 до 20: '))))
    k += 1