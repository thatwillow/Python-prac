#creando una lista (se pueden modificar) (Se empieza desde el valor 0)
lista = ["Carlos Oropeza", "David Alberto", False, 2.80]

#creando una tupla (no se pueden modificar)
tupla = ("Carlos Oropeza", "David Alberto", True, 2.80)

#esto es valido
lista [3] = "Samaera"

#esto no es valido
#tupla[3] = "Samaera

#creando un conjunto (set) (no se accede a elementos por indice) (no almacena datos duplicados)
conjunto = ("Carlos Oropeza", "David Alberto", True, 2.80)

#print(conjunto [3])  no se puede acceder al elemento

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
   'nombre' : "Carlos Oropeza",
    'Steam_code' : "David Pro",
   'Aprendiendo' : True,
   'dato_duplicado' : "David Pro" 
}


print(diccionario['Steam_code'])
print(lista[3])