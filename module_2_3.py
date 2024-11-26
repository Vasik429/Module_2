my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_num = []
a = 0

while a < len(my_list) and my_list[a] >= 0:
    if my_list[a] > 0:
        positive_num.append(my_list[a])
    a += 1
print(positive_num)
a += 1

