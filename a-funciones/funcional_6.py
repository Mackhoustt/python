#Crear una función que calcule la temperatura media de un día a partir de las temperaturas de los ultimos 5 dias.
day_1=int(input("Introduzca la temperatura de los primeros 5 días: "))
day_2=int(input("Introduzca la temperatura de los primeros 4 días: "))
day_3=int(input("Introduzca la temperatura de los primeros 3 días: "))
day_4=int(input("Introduzca la temperatura de los primeros 2 días: "))
day_5=int(input("Introduzca la temperatura de los primeros 1 días: "))
def wheater(day_1,day_2,day_3,day_4,day_5):
  temperature=(day_1+ day_2+ day_3+ day_4 +day_5)/5
  return temperature

print(wheater(day_1,day_2,day_3,day_4,day_5),"°c")
