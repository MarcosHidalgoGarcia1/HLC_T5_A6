import random

def contraseña_generada(longitud_contraseña):
    contraseña = " "
    for i in range(longitud_contraseña):
        contraseña += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + "!#$%&'()*+,-./:;<=>?@[\]^_{|}~" + "0123456789" )
    return contraseña

longitud_contraseña = 8
print(contraseña_generada(longitud_contraseña))