
#---------------------------- Trabajo Práctico 1 de Francisco Gerardi ----------------------------#
#Entrega N°4
#Entrega Final

import random
import os

#Declaro las variables a utilizar:
puntaje = 100
apuesta = 0
apuesta_defecto = 10
apuesta_min = 1

#Utilizaré esta variale para el bucle for
cont_juego = 1

#Declaro las listas que utilizaré:
result = []
list_char = ["A", "B", "C", "D", "E", "0", "7"]

#Para aclarar los premios: 
#Triple 7: 
#   apuesta * 10
#Triple carácter: 
#   apuesta * 5
#Triple 0: 
#   apuesta * 0
#Doble carácter:
#   apuesta * 2
#Ninguna coincidencia: 
#   apuesta * 1

#-------------------------------------------#
#Interfaz y operaciones del juego:

opcion = input("Presionar cualquier botón para iniciar a jugar: ")

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

print("""#----------------------------------------#\n
¡¡¡Bienvenido al tragamonedas virtual!!!\n
#----------------------------------------#\n
Su Puntaje inicial es de:""", puntaje,"""

Apuesta por defecto = 10 [Seleccionar --> '0']

Apuesta personalizada: Mínima = 1 | Máxima = Puntaje

#----------------------------------------#\n""")

apuesta = int(input("Ingrese total a apostar: "))

print("\n#----------------------------------------#\n")
while cont_juego == 1:

    if(puntaje == 0):
        print("\nTu puntaje = 0... Fin del juego.")
        print("#----------------------------------------#")
        break

    match (apuesta):
        case 0:
            apuesta = apuesta_defecto
            continue

#El bucle while() es para cuando la apuesta es menor a la puesta mínima o cuando la apuesta es mayor a tu puntaje
    while(apuesta < apuesta_min or apuesta > puntaje):
        if(apuesta < apuesta_min):
            print("La apuesta mínima es de: 1\n")
            print("Tu puntaje es:", puntaje)
            apuesta = int(input("\nIngrese nuevamente un total a apostar: "))
            print("\n#----------------------------------------#")

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

        elif(apuesta > puntaje):
            print("La apuesta máxima no puede ser mayor a tu puntaje.\n")
            print("Tu puntaje es:", puntaje)
            apuesta = int(input("\nIngrese nuevamente un total a apostar: "))
            print("\n#----------------------------------------#")

            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

#Las siglas son por como estaban puestas antes: pri_char_pantalla | seg_char_pantalla | ter_char_pantalla
    p_c_p = list_char [random.randint(0, len(list_char)- 1)]
    s_c_p = list_char [random.randint(0, len(list_char)- 1)]
    t_c_p = list_char [random.randint(0, len(list_char)- 1)]
    
    print("|",p_c_p,"|",s_c_p,"|",t_c_p,"|")

    result += [p_c_p]
    result += [s_c_p]
    result += [t_c_p]

#Para las 3/3 coincidencias:
    if(result[0] == result[1] and result[0] == result[2]):
        match(result[0]):
            case "7":
                puntaje = puntaje + apuesta * 10
                print("\n¡¡Triple 7!! Puntaje:",puntaje)
            case "0":
                puntaje = apuesta * 0
                print("\nPerdiste todo. Puntaje:",puntaje)
            case _:
                puntaje = puntaje + apuesta * 5
                print("\n¡¡Triple Coincidencia!! Puntaje:",puntaje)

#Para las 2/3 coincidencias:
    elif(result[0] == result[1] or result[0] == result[2] or result[1] == result[2]):
        puntaje = puntaje + apuesta * 2
        print("\n¡¡Doble Coincidencia!! Puntaje:",puntaje)

#Para cuando no hay ninguna coincidencia:
    elif(result[0] != result[1] and result[0] != result[2] and result[1] != result[2]):
        puntaje = puntaje - apuesta * 1
        print("\nNada... Puntaje:",puntaje)

    result = []

    print("\n#----------------------------------------#")
    print("\nTu puntaje es: ", puntaje)

    if(puntaje == 0):
        print("\nTu puntaje es 0... Fin del juego.")
        print("\n#----------------------------------------#")
        break

    cont_juego = int(input("""
Desea seguir jugando...
[1] Si
[0] No

------>: """))
    print("\n#----------------------------------------#")

#Un bucle while que se siga ejecutando hasta seleccionar un valor válido [1] o [0]
    while(cont_juego != 1 and cont_juego != 0):
            cont_juego = int(input("""
Seleccionar las opciones válidas.

Desea seguir jugando...
[1] Si
[0] No

------>: """))
    if(cont_juego == 0):
        print("\nFin del Juego.")
        break

    print("\nTu puntaje es: ", puntaje)

    apuesta = int((input("\n[Apretar '0' para la apuesta por defecto (10)]\n\nIngrese total a apostar: ")))
    print("#----------------------------------------#")

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
#-----------------------------------------------------------------#
