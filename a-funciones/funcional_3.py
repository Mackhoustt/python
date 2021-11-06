#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma: $suma = \frac{n * (n+1)}{2}$
n=int(input("Introduzca numeros: "))
def programa(n):
  result=  n * (n + 1) / 2
  return "El numero inicial es: ",n, "y el resultado es: ",result

print(programa(n))