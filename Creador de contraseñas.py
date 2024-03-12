import random

use = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def Password():
    limit = int(input("Introduzca limite de caracteres:"))
    password = ""

    for i in range(limit):
        select = random.choice(use)
        password += select
    print("Contraseña formada:", password, "\n¡Gracias por utilizar nuestro generador de contraseñas!")


Password()
