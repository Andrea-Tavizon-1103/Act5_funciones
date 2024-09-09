print("funciones creadas por el usuario")
#las funciones
def milista():
    amigos=["su", "diana", "rodo"]
    for tavizon in amigos:
        print(tavizon) 
#llamadas de funcion
milista()
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
#mi diccionario
print("Mi diccionario:")
dicc = {
    "dia": 9,
    "mes": "Septiembre",
    "año": 2024,
    "colores": ["verde", "blaco", "rojo"]
}
print(dicc)
for x in dicc:
    print(x)
    print(dicc[x])
#mis conjuntos
print("Mis conjuntos:")
animales=("perro", "gato", "pajaro", "tigre")
print(animales)

for x in animales:
    print (x)
