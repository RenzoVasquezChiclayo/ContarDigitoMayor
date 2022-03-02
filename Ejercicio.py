
numeros = []

for i in range(0,2):
    print("Ingrese el numero:")
    num = input()
    numeros.append(num)
    
if len(numeros[0])>len(numeros[1]):
    print("El numeros con mas digitos es: " + numeros[0])
else:
    print("El numeros con mas digitos es: " + numeros[1])
