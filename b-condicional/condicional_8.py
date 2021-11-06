#Un año es bisiesto si es divisible por 4, excepto si es una centuria, que tiene que ser divisible por 400 (1800 y 1900 no fueron bisiestos, pero 1600 y el 2000 sí). Escribe un programa que pida el número de un año y muestre si es bisiesto o no.
year=int(input("Introduzca año: "))
def bisiesto(year):
  if year%4 ==0:
    return "bisiesto"
  elif year%100==0:
    return "No es bisiesto"
  elif year%400==0:
    return "bisiesto"
  return "no es bisiesto"
 
print(bisiesto(year))
