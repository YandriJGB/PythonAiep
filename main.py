# crear lista para almacenar las ventas de la semana 
ventas = []
# usar un ciclo para ingresar las ventas 
for i in range(7): #7 dias de la semana 
 venta=float (input(F"ingrese la venta del dia {i+1}:"))
 ventas.append(venta)


 #progresar los datos
 total_ventas = sum(ventas)
print(total_ventas)
promedio_ventas = total_ventas/len(ventas)

#condicion para verificar si se alcanzo la meta 
meta=5000
if total_ventas >= meta:
 mensaje = "felicidades has alcanzado la meta"
else:
 mensaje = "no has alcanzado la meta )"

 #imprimir resultado 
print ("\n---reporte---")
print (f"total de ventas: ${total_ventas}")
print (f"promedio de ventas: ${promedio_ventas}")
print(mensaje)
