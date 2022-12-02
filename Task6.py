import math
def inputNum(numb):
    boolean = True
    while boolean:
        try:
            number = float(input(F"{numb}"))
            boolean = False
        except ValueError:
            print("Введите число!")
    return number
num = inputNum("Введите число: ")
length = len(str(num))
numcel = math.floor(num)
length1 = len(str(numcel))
num = round(num * 10 ** (length - length1 - 1))
summ = 0
while (num != 0):
    summ = summ + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", int(summ))