palabra ="bonita"
iterador = iter(palabra)

for char in iterador:
   print(char)

#iterar con un bucle for y en cadenas string



#ahora con números

limit = 10
el_iterdor = iter(range(0,limit,2))

#va a parar en limit, que es lo mismo que 10, y nno lo muestra por que ese es el límite

for number in el_iterdor:
   print(number)

#iterar con un bucle for y en números


#funcion de fibonacci pasandoe un número como argumento

def fibonacci(numero):   
    a, b = 0, 1
    while a < numero:
        yield a
        a, b = b, a + b

for number in fibonacci(10):
    print(number, "Secuencia fibonacci")