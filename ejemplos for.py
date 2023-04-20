# ejemlo 1
rta= "salida= "

for i in [1,2,3,4,5,6,7,8,9,10]:
    rta=rta+str(i)+" , "
rta=rta +""
print(rta) 

# Ejemplo 2
for i in [1,2,3,4,5,6,7,8,9,10]:
    print("UIS NO ES UNO....")

# Ejemplo 3
for i in (1,2,3,4,5,6,7,8,9,1):
    rta=rta+str(i)+" , "
rta=rta +""
print(rta) 

# Ejemplo 4
rta="salida="
for i in range(1,11):
    rta=rta+str(i)+" , "
print(rta) 

# Ejemplo 5
rta="salida="
for i in "UIS NO ES UNO":
    rta=rta+str(i)+" , "
rta=rta +""
print(rta) 

# Ejemplo 6
suma=0
for i in range(1,11):
    suma=suma +i 
print("La suma es {suma}")

# Ejemplo 7
frase=input("Digite una frase")

vocales="aeiouAEIOU"
numero_vocales=0
for i in frase:
   numero_vocales= numero_vocales+1
print(f"En a frase hay{numero_vocales} vocales")

