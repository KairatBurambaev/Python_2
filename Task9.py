def inputlistN(inputlistN):
    while True:
        try:
            num = int(input(inputlistN))
            num = list(range(-num,num+1))
            return num
        except ValueError:
            print('Введите число!')

index = open('file.txt', 'r')
N = inputlistN('Введите N: ')
position = []
result = 0

for i in index:
    if i != ' ':
        i = int(i)
        position.append(i)
index.close()

#import random #(для перемешивания списка)
#random.shuffle(N) #(для перемешивания списка)

result = N[position[0]] * N[position[1]]
print('Список: ',N,'\nпозиции из file.txt: ',position,'\nПроизведение: ',result)