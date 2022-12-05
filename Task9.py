def inputlistN(inputlistN):
    while True:
        try:
            Num = int(input(F'{inputlistN}'))
            Num = list(range(-Num,Num+1))
            return Num
        except ValueError:
            print('Введите число!')
    return Num
index = open('file.txt', 'r')
N = inputlistN('Введите N: ')
list_var = []
result = 0
for i in index:
    if i != ' ':
        i = int(i)
        list_var.append(i)
index.close()
#import random #(для перемешивания списка)
#random.shuffle(N) #(для перемешивания списка)
result = N[list_var[0]] * N[list_var[1]]
print('Список: ',N,'\nпозиции из file.txt: ',list_var,'\nПроизведение: ',result)