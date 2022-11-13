import datetime

###Datos persona Fase 1###
numeroDeIdentificacion = int(input("Escriba su número de identificación: "))
nombres = input("Escriba su(s) nombre(s): ")
apellidos = input("Escriba sus apellidos: ")
direccion = input("Digite su dirección: ")
telefono = int(input("Número de teléfono: "))
genero = input("Con qué género se identifica: ")
estadoCivil = input("Estado civil: ").upper()
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
diasTrabajados = int(input("¿Cuántos días trabajó este mes? "))
###Fin Datos de la persona###


###Bonos Fase 2###
if edad > 55:
    bonoEdad = sueldo * 0.05
    sueldo += bonoEdad
    print("""
          ---------------------------------------------------------
          ***Felicitaciones tiene un bono del 5% por su edad***
          ---------------------------------------------------------
          """)
fechaFundacion = datetime.date(1984,4,2)
diaFundacion = fechaFundacion.strftime("%d%m")
diaCumple = fechaNacimiento.strftime("%d%m")
if diaFundacion == diaCumple:
    print("""
          ---------------------------------------------------------
          ***Felicitaciones por cumplir el mismo día de la 
          fundación de la empresa, haremos una fiesta***
          ---------------------------------------------------------
          """)
if estadoCivil == "CASADO" and hijos == "SI":
    print("""
          ---------------------------------------------------------
          ***Felicitaciones por estar casado(a) y tener hijos 
          la empresa le otorgará un viaje cada Diciembre***
          ---------------------------------------------------------
          """)
if sueldo >= 1000000 and sueldo <= 1500000:
    bonoSueldo = sueldo * 0.02
    sueldo += bonoSueldo
    print("""
          ---------------------------------------------------------
          ***Felicitaciones tiene un bono del 2% por tu salario***
          ---------------------------------------------------------
          """)
elif sueldo > 1500000 and sueldo <= 2000000:
    bonoSueldo = sueldo * 0.05
    sueldo += bonoSueldo
    print("""
          ---------------------------------------------------------
          ***Felicitaciones tiene un bono del 5% por tu salario***
          ---------------------------------------------------------
          """)
if diasTrabajados >= 20 and sueldo < 1000000:
    print("""
          ---------------------------------------------------------
          ***Felicitaciones tiene derecho a un bono de alimentación***
          ---------------------------------------------------------
          """)
###Fin Bonos Fase 2###

###Tipo de contrato Fase 3###
###Fin Tipo de contrato Fase 3###

###Cantidades Fase 4###
###Fin Cantidades Fase 4###


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
      Ha trabajado: {13} días este mes
      
      
      """.format(numeroDeIdentificacion,nombres,apellidos,direccion,telefono,genero,estadoCivil,hijos,cuantosHijos,estatura,fechaNacimiento,edad,sueldo,diasTrabajados))