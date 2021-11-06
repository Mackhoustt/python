#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es imc donde imc es el índice de masa corporal calculado redondeado con dos decimales.
peso=int(input("Inserte su peso: "))
estatura=int(input("Inserte su estatura: "))
estatura_2=estatura/100
def IMC(peso, estatura_2):
  imc= peso / estatura_2**2
  return imc



print("tu Indice IMC es: ",round(IMC(peso, estatura_2),2))
