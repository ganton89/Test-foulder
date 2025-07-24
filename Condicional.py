x = 10

if x > 5:
    print("x is greater than 5") 
elif x == 5:
    print("x is equal to 5")
else:
    print("x is not greater than 5")

# Another example with conditional statements

y = 10

if y > 5 and x < 15:
    print("Se cumple la condicion y esta entre 5 y 15")
else:
    print("No se cumple")

# ahora un ejemplo con if anidados

is_member = False
age = 3

if is_member:
    if age >= 18:
        print("Puedes entrar al club")
    else:
        print("Debes ser mayor de edad para entrar al club")    

else:
    print("Debes ser miembro para entrar al club")



