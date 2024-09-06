#Lee un número por teclado que pida el precio de un producto (puede tenerdecimales) 
# y calcule el precio final con IVA. El IVA sera una constante que sera del 21%. 

precio=float(input("ingrese el precio del producto"))      #el float cambia el texto en un numero real o decimal
precioFinal= precio + precio* 0.21
print("el precio final del producto es:   ", precioFinal)