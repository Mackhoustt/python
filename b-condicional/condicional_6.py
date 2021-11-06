#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
vegetariana=str(input("Introduzca si desea es vegetariana ""Si " "No "": "))
ingredientes_vegan=str(input("Introduzca un ingrediente vegetariana ""Pimiento " "Tofu: """))
ingrediente=str(input("Introduzca un ingrediente ""Peperoni " "Jamón " "Salmón: """))
def pizza(vegetariana, ingredientes_vegan, ingrediente):
  vegetariana="Si"==True
  vegetariana="No"==False
  if vegetariana == "Si" and ingredientes_vegan=="Pimiento":
    return "Pizza vegetariana con pimiento, mozzarella y el tomate"
  elif vegetariana == "Si" and ingredientes_vegan=="Tofu":
    return "Pizza vegetariana con Tofu, mozzarella y el tomate"
  elif vegetariana=="No" and ingrediente=="Peperoni":
    return "Pizza con Peperoni, mozzarella y el tomate"
  elif vegetariana=="No" and ingrediente=="Peperoni":
    return "Pizza con Jamón, mozzarella y el tomate"
  elif vegetariana=="No" and ingrediente=="Peperoni":
    return "Pizza con Salmón, mozzarella y el tomate"
  return "no se ha seleccionado un tipo de pizza"
#Ingredientes vegetarianos: Pimiento y tofu.
print(pizza(vegetariana, ingredientes_vegan, ingrediente))
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.