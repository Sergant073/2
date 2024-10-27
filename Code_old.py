
def find_pairs(target):
    password = ''

    for i in range(1, target // 2 + 1):
        for j in range(i + 1, target + 1 - i):
            if target % (i + j) == 0:
                password += str(i) + str(j)
    return password

# for target in range(3, 21):
#     pairs = find_pairs(target.int(input))
#     print(f"Уникальные пары для числа {target}: {pairs}")
n = int(input('Ведите число от 3 до 20: '))
result = find_pairs(n)
print('Пароль:', result)