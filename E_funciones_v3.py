#las tuplas
print("Mis tuplas:")
numeros=(1,2,3 ,4)
print(numeros)
print("-rango de numeros")
print(len(numeros))
print("elemento de los numeros")
print(numeros[3])
y = list(numeros)
y[1] = "5"
x = tuple(y)
print (x)
for num in numeros:
    print(num)