#Dada dos numeros y un string que indique el tipo de operación realice la operación aritmetica, las operaciones validas son "+", "-", "*", "/", "**".
x=int(input("Introduzca número: "))
y=int(input("Introduzca número: "))
tipo=str(input("Introduzca tipo:+" "-" "*" "/" "**"))
def formula(x,y,tipo):
  if tipo=="+":
    return x+y
  elif tipo=="-":
    return x-y
  elif tipo=="*":
    return x*y
  elif tipo=="/":
    return x/y
  elif tipo=="**":
    return x**y
  return "Por favor, introduzca un valor valido"

print(formula(x,y,tipo))