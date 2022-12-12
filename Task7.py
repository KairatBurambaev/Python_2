def inputN(inputN):
    while True:
        try:
            Num = int(input(inputN))
            return Num
        except ValueError:
            print("Введите число!")

N = inputN("Введите N: ")

def fu(x):
    if x == 1:
        return 1
    else:
        return x * fu(x-1)

list = [fu(i) for i in range(1, N+1)]

print(f"Произведения чисел от 1 до {N}:  {list}")