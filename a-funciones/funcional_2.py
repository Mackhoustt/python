#Escriba una función que tome kilometros y los transforme a metros.
km=int(input("Introduzca Kilometros: "))
def conversor(km):
  meters= km*1000
  return meters
  result=meters

print(conversor(km),"m",end="")
