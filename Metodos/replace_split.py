cadena1 = "ceremonia,en,mi,casa,bro"
cadena2 = "a david le gustan las minas"
cadena3 = "quererse"

#REPLACE

#verifica si la cadena empieza con un caracter o una palabra especifica, si es asi devuelve True
empieza_con = cadena1.startswith("c")
starts = cadena2.startswith("S")
empistarts = cadena3.startswith("q")

print(empieza_con)
print(starts)
print(empistarts)

#SPLIT

#Separa todo y crea una lista

cadena_separada = cadena1.split(",")
print(cadena_separada)