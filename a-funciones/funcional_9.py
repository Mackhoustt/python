#Escribir dos funciones que permitan calcular:

#La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
h=int(input("inserte horas: "))
m=int(input("inserte minutos: "))
s=int(input("inserte segundos: "))
def hours_seconds(h,m,s):
  result=(h*3600)+(m*60)+(s*1)
  
  return result

print(hours_seconds(h,m,s),"s")

toh=int(input("inserte segundos: "))

def seconds_hours(toh):
  minutos=toh//60
  seconds2=toh%60
  horas=minutos//60
  minutos2=minutos%60
  return (horas,"h", minutos2,"m", seconds2,"s")
  

print(seconds_hours(toh))