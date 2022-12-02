def inputN(inputN):
    boolean = True
    while boolean:
        try:
            Num = int(input(F"{inputN}"))
            boolean = False
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