# square = [x**2 for x in range(1, 11)]
# print(square)
# print(square[0:5])  # Imprime los primeros 5 cuadrados

# celsius = [0,10,20,30,40,50]

# farhenheit = [((9/5) * temp + 32) for temp in celsius]
# print(farhenheit)

# events = [n for n in range(1,21) if n % 2 == 0]
# print(events)  # Imprime los números pares del 1 al 20

# Obtener la traspuesta de una matriz

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print(len(matrix[0]))

prueba = range(len(matrix[0]))
print(prueba)    


transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print (matrix)  # Imprime la matriz original
print(transpose)  # Imprime la matriz traspuesta