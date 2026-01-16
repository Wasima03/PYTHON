from datetime import date,time,datetime, timedelta

hoy =date.today() #fecha de hoy
print(hoy)
ahora=datetime.now() #fecha y hora de hoy
print(ahora)

hora=time(7,22,15)
fecha=date(2020,12,31)
momento=datetime(1876,10,8,12,34)
print(hora)
print(fecha)
print(momento)

formateado=momento.strftime("%d/%m/%Y")
print(formateado)
print(momento.strftime("%A %d/%B/%Y"))

texto="2025-01-03 14:30"
formato="%Y-%m-%d %H:%M"
objeto=datetime.strptime(texto,formato)
print(objeto)
print(objeto.year)
print(objeto.month)
print(objeto.day)

fechaFutura=objeto+timedelta(days=3456, hours=2, weeks=12)
print(fechaFutura)

