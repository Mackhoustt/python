#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter. multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"
n=int(input("Introduzca numeros: "))
x=str(input("Introduzca letra: "))
def generar_n_caracteres(n,x):
  result=x*n
  return result
print(generar_n_caracteres(n,x))
  
