first = int(input ("Ведите первое число:"))
second = int(input("Ведите ыторое число:"))
third = int(input("Введите третье число:"))
if first == second == third:
    print("Ответ: 3")
elif first == second or first == third or second == third:
    print("Ответ: 2")
else:
    print("Ответ: 0")