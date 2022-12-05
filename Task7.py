def inputN(inputN):
    while True:
        try:
            Num = int(input(F"{inputN}"))
            return Num
        except ValueError:
            print("Введите число!")
    return Num
N = inputN("Введите N: ")
def fuu(x):
    if x == 1:
        return 1
    else:
        return x * fuu(x-1)
list = []
for i in (range(1,N+1)):
    list.append(fuu(i))
print(f"Произведения чисел от 1 до {N}:  {list}")