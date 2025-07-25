number = [1,2,3,4,5,6]
x=2

contador = 0
while contador < 5:
    print(contador, "estamos en el bucle while")
    contador += 1
#bucle for, lo que nos muestra es la repetición mientras una variable esta dentro de un rango
# Se repetirá las veces que tenga el rango de la lista

for i in number:
    print(i, "es el valor de la lista, estamos en el bucle for")
    print(number[i-1])


    #Ahora voy a probar con el bucle for con un rango


    suma = 0

for i in range(1, 100):
    print("Número actual:", i)
    suma += i
    print("Suma parcial:" , suma)
    
    if suma >= 20:
        print("¡Se alcanzó el límite!")
        break


#Cotraseña erronea, pequeño programa de tres intenmtos para introducir la contraseña correcta# Definición de la contraseña correcta

clave = "Pisco.2025"
intentos = 0
# Bucle para solicitar la contraseña hasta 3 intentos
while intentos < 3:
    entrada = input("Introduce la contraseña: ")
    if entrada == clave:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Te quedan {3 - intentos} intentos.")
 
   

