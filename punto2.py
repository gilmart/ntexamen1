#Leer el nombre de 10 frutas {nombre, color, precio} para preparar un
#salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al
#mismo tiempo en sentido inverso al ingresado+(1)


#Nombre
#color
#Precio

print("***MENU***")
print("1. Agregar fruta")
print("2. Mostrar mostrar")
print("3. SALIR")
opcion=100

frutas=[]
suma=1

while(opcion!=3):
    fruta={}
    opcion=int(input('Digite una opcion: '))
    if(opcion==1):
        for centinela in range (1):
            fruta['nombre']=input(f'digit el sabor de la frut {suma}: ')
            fruta['color']=input('digit el color: ')
            fruta['precio']=int(input('digit el precio: '))
            suma=suma+1
            frutas.append(fruta)

    elif(opcion==2):
        for fruta in frutas[::-1]:
            print(fruta)


