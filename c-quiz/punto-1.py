temp=int(input("inserte Valor: "))
tipo=(input("De que tipo es: ").upper())
def calcular(temp,tipo):
    if tipo=="F":
        result=(temp-32)* 5/9 
        print (f"\nLa temperatura {temp}°F es {result} en Celsius")
    elif tipo== "C":
        result2=(temp + 32) * 9/5  
        print (f"\nLa temperatura {temp}°C es {result2} en Fahrenheit")
    return "no se ha regresado un valor"
print(calcular(temp,tipo),end="")