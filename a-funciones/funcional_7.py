#Diseñar una función que calcule el área y el perímetro de una circunferencia.
radius=int(input('radio: '))
pi=3.1417
def circunference_perimeter(radius,pi):
  circunference=2*pi*radius
  area=pi*radius**2
  return area, circunference

print("el area y perimetro son: ",circunference_perimeter(radius,pi))