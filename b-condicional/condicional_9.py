#Una empresa de bienes raíces ofrece casas de interés social, bajo las siguientes condiciones:

#Si los ingresos del comprador son de 8000 o más el enganche será del $15%$ del costo de la casa y el resto se distribuirá en pagos mensuales, a pagar en diez aos.
#Si los ingresos del comprador son menos de 8000 el enganche será del $30%$ del costo de la casa y el resto se distribuirá en pagos mensuales a pagar en 7 años.
#La empresa quiere obtener cuánto debe pagar un comprador por concepto de enganche y cuánto por cada pago parcial.

ingresos=int(input("ingresos: "))
costo_casa=int(input("Valor casa: "))
def prestamo(ingresos,costo_casa):
  if ingresos>8000:
    valor=costo_casa*(15/100)
    final=(costo_casa-valor)/120
    return (valor, final)
  elif ingresos<=8000:
    valor2= costo_casa*(30/100)
    final=(costo_casa-valor2)/84
  return (valor2, final)
print("el valor del pago inicial y pagos mensuales serán: ",prestamo(ingresos,costo_casa))