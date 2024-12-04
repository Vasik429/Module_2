for n in range (3, 21):
    password = []
    for i in range(1, 20):
        for j in range(2, 20):
            if n % (i + j):
                while n >= (i + j) and n % (i + j):
                    password.append(i)
                    password.append(j)
print(password)

