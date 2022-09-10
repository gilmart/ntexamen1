#Construir un programa que permita ingresar N (cantidad digitada por el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron ingresados (+1)

numeros=int(input(f'digite la cantidad de numeros '))
dato=1
lista=[]
while(dato <= numeros):
    numero= int(input(f'Digite numero {dato}: '))
    dato=dato+1

    if(numero%2==0 or numero%3==0):
        lista.append(numero)
    print(len(lista))


