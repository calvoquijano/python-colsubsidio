from datetime import date, datetime
numeroDeIdentificacion = int(input("Escriba su número de identificación: "))
sueldo = int(input("¿Cuánto se gana? $"))
fechaActual = datetime.now()
anio = int(input('Año de nacimiento: '))
mes = int(input('Mes de nacimiento: '))
dia = int(input('Día en el que nació: '))
fechaNacimiento = date(anio,mes,dia)
anios = int(date.strftime(fechaActual, "%Y"))
edad = anios - anio





print("Su número de ID es {0} ${1:,.2f}\n{0}{1}{2}{3}".format(numeroDeIdentificacion,sueldo,edad,fechaNacimiento))