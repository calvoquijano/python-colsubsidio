import datetime


###Datos de la persona###
numeroDeIdentificacion = int(input("Escriba su número de identificación: "))
nombres = input("Escriba su(s) nombre(s): ")
apellidos = input("Escriba sus apellidos: ")
direccion = input("Digite su dirección: ")
telefono = int(input("Número de teléfono: "))
genero = input("Con qué género se identifica: ")
estadoCivil = input("Estado civil: ")
#Hijos
hijos = input("¿Tiene hijos?(Si/No) ").upper()
if hijos == "SI":
    cuantosHijos = int(input("¿Cuántos? "))
elif hijos == "NO":
    cuantosHijos = "No tiene"
else:
    cuantosHijos = "Respuesta inválida, vuelva a responder por favor."
    print(cuantosHijos)
    while hijos!="SI":
        hijos = input("¿Tiene hijos?(Si/No) ").upper()
        if hijos == "SI":
            cuantosHijos = int(input("¿Cuántos? "))
            break
        elif hijos == "NO":
            cuantosHijos = "No tiene"
            break
        else:
            cuantosHijos = "Respuesta inválida"
        hijos = "Diferente"
#Fin de hijos
estatura = float(input("¿Cuánto mides? "))
fechaActual = datetime.datetime.now()
anio = int(input('Año de nacimiento (completo): '))
mes = int(input('Mes de nacimiento (número): '))
dia = int(input('Día en el que nació (número): '))
fechaNacimiento = datetime.date(anio,mes,dia)
anios = int(datetime.date.strftime(fechaActual, "%Y"))
edad = anios - anio
sueldo = int(input("¿Cuánto es su sueldo al mes? $"))
diasTrabajados = int(input("¿Cuántos días lleva trabajando? "))
###Fin Datos de la persona###


print("""
      
      Cédula de ciudadanía: {0}
      Nombres: {1}
      Apellidos: {2}
      Dirección: {3}
      Teléfono: {4}
      Edad: {11}
      Género: {5}
      Estado civil: {6}
      Tiene hijo(s)(as): {7}
      Cuántos: {8} hijo(s)(as)
      Mide: {9} m
      Fecha de nacimiento: {10}
      Su salario es de: ${12:,.2f}
      Ha trabajado: {13} días
      
      
      """.format(numeroDeIdentificacion,nombres,apellidos,direccion,telefono,genero,estadoCivil,hijos,cuantosHijos,estatura,fechaNacimiento,edad,sueldo,diasTrabajados))