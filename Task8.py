def inputN(inputN):
    while True:
        try:
            Num = int(input(F"{inputN}"))
            return Num
        except ValueError:
            print("Введите число!")
    return Num
list_variable = inputN("Введите N: ")
my_list = []
for i in range(1,list_variable+1):
    elem = (1+1/i)**i
    my_list.append(elem)
print(f"{list_variable}:  {(my_list)}")