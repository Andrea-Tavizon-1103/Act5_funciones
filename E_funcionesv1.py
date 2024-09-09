print("manejo de funciones v1")
def hola_mundo():
    print("hola aqui estoy dentro de la funcion")

def mensa(msg):
    print(msg)
def escribenc (nombre,apellido):
    print(nombre,apellido)
    print(f"tu nombre completo es {nombre} {apellido} ")
def suma2num(n1, n2):
    s=n1+n2
    return f"la suma de {n1} y de {n2} es de: ", s
#  print (f" la suma de {n1} mas {n2} es {s}")
# llamando la funcion
hola_mundo()
mensa("hola wasap") #llama a la funcion mensa con 1 parametro
mensa("el profe me sorprendio enviando mensajes") #llama a mensa con 1 parametro
escribenc("Andrea", "Tavizon")
print("funciones que regresan valores")
print(suma2num(7,3))
print (suma2num(15,45))