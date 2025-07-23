cadena1 = "ceremonia en mi casa bro"
cadena2 = "a david le gustan las minas"
cadena3 = "quererse"

#Buscamos un caracter o una palabra con este codigo, si la letra o palabra no existe saldra -1
busqueda_find = cadena1.find("s")
print(busqueda_find)

#lo mismo que find pero si no encuentra coincidencias nos tira una excepcion
busqueda_index = cadena1.index("s")
print(busqueda_index)