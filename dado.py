import random
lado1=0;lado2=0;lado3=0; lado4=0; lado5=0; lado6=0;
cont=0

list = [0,0,0,0,0,0]


for i in range(100):
    lados = random.randint(1,6)
    print(lados)
    list[lados-1]+= 1  

for i, contagem in enumerate(list, start=1):
    print(f'{i}| {contagem}')