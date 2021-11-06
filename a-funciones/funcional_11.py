#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

#Usando interes simple.
prestamo = int(input('dinero prestado: '))
time = int(input('Tiempo: '))
interes =int(input('Interes: '))

def interes_simple(prestamo,time,interes):
	interes=interes/100
	return prestamo*time*interes

print("Su interés es: ",interes_simple(prestamo,time,interes))
#Usando interes compuesto.

prestamo_2=int(input('dinero prestado: '))
tiempo=int(input('Tiempo: '))
interes_base=int(input('Interes: '))

def interes_compuesto(prestamo_2,tiempo,interes_base):
  interes_base=interes_base/100
  return prestamo_2*(1+interes_base)*tiempo

print("Su interés compuesto es: ", interes_compuesto(prestamo_2,tiempo,interes_base))