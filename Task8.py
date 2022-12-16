def inputN(inputN):
    while True:
        try:
            num = int(input(inputN))
            return num
        except ValueError:
            print("Введите число!")

num = inputN("Введите N: ")

fu = lambda x: (1+1/x)**x

new_list = list(map(fu,[i for i in range(1, num+1)]))

print(f"{num}: {(new_list)}")