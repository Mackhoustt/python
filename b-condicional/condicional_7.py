#Escribe un programa que pida la nota de un estudiante (de 1 a 10) y diga si es un insuficiente (menos de 5), suficiente (de 5 a 7), notable (de 7 a 9) o sobresaliente (entre 9 y 10).
grade=int(input("Introduzca número: "))
def student_grade(grade):
  if grade<5:
    return "insuficiente"
  elif grade<=7:
    return "suficiente"
  elif grade<9:
    return "notable"
  return "sobresaliente"

print(student_grade(grade))