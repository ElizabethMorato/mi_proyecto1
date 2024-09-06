#Lee un número por teclado e indica si es divisible entre 2 (resto = 0). 
#Si no lo es,también debemos indicarlo. 
numero=int(input("ingrese un numero"))   # el int() lo que ingresa a dentro lo convierte en un numero entero
modulo=numero % 2
if modulo==0:
    print("el numero es divisible por 2")
else:
    print("el numero no es divisible por 2")