def Password (number):
    pass_ = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_


result1 = Password(5)
print(result1)


# num = set(range(3, 21))
# print(num)
#
# def find_pass (*numbers):
#     pass_ = ''
#     for i in range(1, 21):
#         for j in range(i + 1, numbers):
#             if numbers % (i + j) == 0:
#                 pass_ += str(i) + str(j)
#     return pass_
#
# result2 = find_pass(num)
# print(result2)
