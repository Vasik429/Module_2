my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_num = []
a = 0

while a < len(my_list) and my_list[a] >= 0:
    if my_list[a] > 0:
        positive_num.append(my_list[a])
    a += 1
print(positive_num)
a += 1


fruts = ["apple", "banana", "cherry", "date", "", "fig", "grape"]
Fruts_list = []
i = 0
while i < len(fruts) and fruts[i] != "":
    if fruts[i] != "":
        Fruts_list.append(fruts[i])
    i += 1
print(Fruts_list)
i += 1

u_list = ['apple', 'apricot', 'asparagus', 'nuts', '', 'cucumber', 'apelsin']
up_list = []
u = 0
while u < len(u_list) and u_list[u].startswith("a"):
    print(u_list[u])
    u += 1