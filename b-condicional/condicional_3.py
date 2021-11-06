#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
x=int(input("Introduzca número: "))
def par(x):
  if (x%2)==0:
    return "Es par"
  return "Es impar"
print(par(x))