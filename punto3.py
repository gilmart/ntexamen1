#Construir un programa para ir de compras en un supermercado
#que permita la construcción del siguiente MENU:

#1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
#2. Digitar 2 para mostrar todos los productos registrados (+0.4)
#3. Digitar 3 para permitir buscar por código un producto y editar el precio de este (+0.4)
#4. Digitar 4 para permitir buscar por código un producto y eliminar el producto (+0.4)
#5. Digitar 0 para SALIR



print("***MENU***")
print("1. RECIBIR PRODUCTO")
print("2. MOSTRAR LOS PRODUCTOS INGRESADOS")
print("3. BUSCAR POR CODIGO UN PRODUCTO Y CAMBIAR EL PRECIO")
print("4. BUSCAR POR CODIGO UN PRODUCTO Y ELIMINAR EL PRODUCTO")
print("5. SALIR")

opcion=100
productos=[]

while(opcion != 0):
    producto={}
    opcion=int(input(f'DIGITE UN OPCION: '))
    if (opcion==1):
        producto['codigo']=int(input('Digite el codigo: '))
        producto['nombre']=input('Digite le nombre: ')
        producto['precio']=int(input('Digite el precio: '))
        productos.append(producto)

    elif(opcion == 2):
        print(productos)    
    elif(opcion == 3):
       productoNuevo =int(input(f'ingrese el codigo del producto que desee editar: '))
       for prodN in productos:
        codN=prodN
        for codN in productos:
            producto['precio']=int(input('Digite el nuevo precio: '))
            print(producto)
    elif(opcion == 4):
        producto['codigo']=int(input('Digite el producto q desee eliminar: '))
        for producto['codigo'] in productos:
            productos.remove(producto['codigo'])
        print(producto)
   
            

