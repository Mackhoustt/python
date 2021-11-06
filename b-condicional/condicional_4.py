#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
def which_group(name,sex):
  if(sex=="M" and name[0].lower()<"m") or (sex=="H" and name[0].lower()>"n"):
    return "A"
  return "B"

print(which_group("Samuel", "M"))