nombre = "Andrés "#String
apellido = "Quijano "
edad = 38#Int
estatura = 1.75#Double
sueldo = 8750000
ganaBien = True

if ganaBien == True:
    ganaBien = "gana bien"


#Formas de imprimirlo
#Concatenar con + Strings y con , números
print("Mi nombre es "+nombre+apellido+"y tengo",edad,", mido",estatura,"y mi sueldo es de $",sueldo,"\n"+nombre+ganaBien)
#Formato 1
print(f"Mi nombre es {nombre}{apellido}y tengo {edad}, mido {estatura} y mi sueldo es de ${sueldo}\n{nombre}{ganaBien}")
#Formato 2
print("Mi nombre es {}{}y tengo {}, mido {} y mi sueldo es de ${}\n{}{}".format(nombre,apellido,edad,estatura,sueldo,nombre,ganaBien))
#Formato 3 con índices
print("Mi nombre es {0}{1}y tengo {2}, mido {4} y mi sueldo es de ${3:,.2f}\n{0}{5}".format(nombre,apellido,edad,sueldo,estatura,ganaBien))


a = 8<9 or 2>=2
d = 9>=10 and 11>=10
x = "c" < "p"
y = "socio" in "sociopata"#Dentro de 
print(y)

#Formato de Strings
bajas = "ANDRESITO "
mayusculas = "andresito "
quitarEspaciosAntesDespues = "            E S P A C I O       "
titulo = " aNDRESITO "
dosMetodos = quitarEspaciosAntesDespues
print(bajas.lower() + mayusculas.upper() + quitarEspaciosAntesDespues.strip() + titulo.title() + dosMetodos.strip().lower())

#Capturar datos
nombreCapturado = input("Escribe tu nombre: ").upper()
edadCapturada = int(input("Escribe tu edad: "))
print("Tu nombre es: "+nombreCapturado + " y tienes: ",edadCapturada)