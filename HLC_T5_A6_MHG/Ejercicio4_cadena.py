def Palindromo(cadena):
    
    if len(cadena)<=1:
        return True
    
    if cadena[0]!=cadena[-1]:
        return True
    
    return Palindromo(cadena[1:-1])

texto="reconocer"

print(Palindromo(texto))