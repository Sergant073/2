def find_pairs(target):
    password = ''

    for i in range(1, target // 2 + 1):
        for j in range(i + 1, target + 1 - i):
            if target % (i + j) == 0:
                password += str(i) + str(j)
    return password

for target in range(3, 21):
    pairs = find_pairs(target)
    print(f"Уникальные пары для числа {target}: {pairs}")