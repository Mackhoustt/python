#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.
n=int(input("Introduzca numeros: "))
x=int(input("Introduzca numeros: "))
def EsMultiplo(n,x):
  result= x/n
  return result
print(EsMultiplo(n,x))