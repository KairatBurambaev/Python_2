def inputN(inputN):
    while True:
        try:
            num = int(input(inputN))
            return num
        except ValueError:
            print("Введите число!")

num = inputN("Введите N: ")

def fu(i):
    return (1+1/i)**i

new_list = [fu(i) for i in range(1, num+1)]

print(f"{num}: {(new_list)}")