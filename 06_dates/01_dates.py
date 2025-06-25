#Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

#fecha y hora actual
print(datetime.now()) 


#crear fecha y hora especifica

specific_date = datetime(2026, 1, 4)
print(specific_date)

#formatear fechas
now = datetime.now()
format_date = now.strftime("%d/%m/%y %H:%M:%S")
print(format_date)


#Operaciones con fechas

yesterday = datetime.now() - timedelta(days=1, hours=1)
print(f"Ayer: {yesterday}")



#fechas en otro idioma

