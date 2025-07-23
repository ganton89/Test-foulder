a = [1,2,3,4,5]
b= a
print(b)
print(a)
print("----------")
del a[-1]
print(id(a))
print(id(b))
c=a[:]
print(c)
print(id(c))
# Vamos a ver las diferencias entre las listas
# a y b, y la lista c   

print("----------")
a.append(6)
print(a)    
print(b)
print(c)
print("----------")