def inputNum(numb):
    while True:
        try:
            num = float(input(numb))
            return num
        except ValueError:
            print("Введите число!")

num = inputNum("Введите число: ")
res = 0

for i in str(num):
    if i != '.':
        res = res + int(i)

print("Сумма цифр числа равна: ", res)