def greet (name):
  name = input("Ingrese su nombre: ")
  print("Hola", name,"!")


def sumatorio(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + sumatorio(n - 1)

print(sumatorio(5))  # Imprime 15, que es 5 + 4 + 3 + 2 + 1



