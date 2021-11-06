#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
usuario=str(input("Introduzca usuario: "))
contraseña=str(input("Introduzca contraseña: "))
def Login(usuario, contraseña):
  
  return (usuario=="usuario1" and contraseña=="asdasad")

print(Login(usuario, contraseña))