def inputN(inputN):
    boolean = True
    while boolean:
        try:
            Num = int(input(F"{inputN}"))
            boolean = False
        except ValueError:
            print("Введите число!")
    return Num
list_variable = inputN("Введите N: ")
my_list = []
for i in range(1,list_variable+1):
    elem = (1+1/i)**i
    my_list.append(elem)
print(f"{list_variable}:  {(my_list)}")