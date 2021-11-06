#Dado un numerero de 1 al 7, escribir un programar que imprima el dia, por ejemplo Lunes, Martes, etc, si el numero es menor a 1 o mayor a 7 imprimir dia invalido.
number=int(input("Introduzca número: "))
def day(number):
  if number==1:
    return "Lunes"
  elif number==2:
    return "Martes"
  elif number==3:
    return"Miercoles"
  elif number ==4:
    return "Jueves"
  elif number ==5:
    return "Viernes"
  elif number ==6:
    return "Sábado"
  elif number ==7:
    return "Domingo"
  return "Error"

print(day(number))