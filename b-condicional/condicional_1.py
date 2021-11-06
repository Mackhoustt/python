#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
yrld=int(input("Introduzca edad: "))
def is_adult(yrld):
  if yrld<18:
    return "Menor de edad"
  return "Mayor de edad"

print(is_adult(yrld))