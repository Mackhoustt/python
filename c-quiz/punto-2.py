
def triangle_selector(a,b,c):
    if(a==b and a==c):
        return "Equilatero"
    elif(a==b) or (b==c) or (c==a):
        return "Isoseles"
    elif a+b>c and a+c>b and b+c>a:
        return "Escaleno"
    return "No es un triangulo"
a=float(input())
b=float(input())
c=float(input())
print(triangle_selector(a,b,c), end="")