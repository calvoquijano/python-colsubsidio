#Condicionales If intrucción - else: - elif instrucciones
#IF
#Operadores relacionales: > >= < <= == != y lógicos: and or not
estadoAnimo = input("¿Cómo te sientes hoy?: ").upper()
if estadoAnimo == "ALEGRE" or estadoAnimo == "CONTENTO" or estadoAnimo == "FELIZ":
    print("Que bien, me alegro que estés alegre.")
elif estadoAnimo == "TRISTE":
    print("Qué mal.")
else:
    print("No entiendo cómo te sientes")
    
edad = int(input("¿Qé edad tienes? "))
if edad > 0 and edad < 120:
    print("Estás joven")
else:
    print("Pon un valor válido: ")
#Try except
try:
    hijos = int(input("¿cuántos hijos tienes? "))
except ValueError:#Funciona sin el Value Error
    print("Dato incorrecto")

