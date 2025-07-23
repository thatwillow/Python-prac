#LIST
#creando una lista con list(())
lista = list(("David", "Carlos", "Hector", "Santiago", "Ricardo"))

#LEN

#LEN NUMERO DE ELEMENTOS DE LISTA
resultado_caracteres = len(lista)


#APPEND

#APPEND AGREGA ELEMENTOS A LA LISTA ORIGINAL
agregando = lista.append("Constanza")

#INSERT

#Nos agrega un elemento especifico en un lugar de la lista especifico
lista.insert(3, "Orozco")

#EXTEND

#agrega varios elementos a la lista
lista.extend((False, 1))

print(lista)