#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
i=int(input("Introduzca número: "))
j=int(input("Introduzca número: "))
def division(i,j):
  if i>0 and j>0:
    return i/j
  return "error"

print(division(i,j))