# -*- coding: utf-8 -*-

"""Este es un juego que permitira adivinar un numero aleatrio"""

import random
INTENTOS = 0
ERROR = 0
ALEATORIO = random.randint(1, 51)
NOMBRE = raw_input("Ingrese su nombre:")

print "\n¡Hola!"+ NOMBRE +" Bienvenido al Juego Adivina el Número\n"
print "INSTRUCCIONES:\n"
print """En Este Juego debes adivinar un número del 1 al 50, tendrás únicamente
8 intentos para encontrar el número.\n"""

# While que cuenta los intentos del usuario
while INTENTOS < 8:
    INTENTOS = INTENTOS+ 1
    print "Elige un número"
    NUMERO = raw_input()

    try:
        NUMERO = int(NUMERO)
        ERROR = 1
    except ValueError:
        print "solo puedes ingresar números"
        ERROR = 0
        INTENTOS = INTENTOS + 1

    if NUMERO > 50 or NUMERO < 1:
        print "Inentalo de nuevo."
    if ERROR == 1 or ERROR > 1:
        if NUMERO < ALEATORIO:
            print "Tu número es mas bajo\nIntentalo de nuevo\n"
        if NUMERO > ALEATORIO:
            print "Tu número es mas alto\nIntentalo de nuevo\n"
        if NUMERO == ALEATORIO:
            break

if NUMERO == ALEATORIO:
    print"¡CORRECTO! ¡USTED GANA!"

if NUMERO != ALEATORIO:
    print"¡INCORRECTO!\n¡JUEGO TERMINADO!"
