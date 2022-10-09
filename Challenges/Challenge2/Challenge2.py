#Exercise here ("https://drive.google.com/file/d/1OtYBpjBehrMW5GQshdjj9vEmfXRuZ6xu/view?usp=sharing")

def encriptador(mensaje):
    letters = list(mensaje)
    unique = set(letters)
    clave = dict(zip(unique, alfabeto))
    encriptado = ''
    for letter in letters:
        encriptado += clave[letter]
    return encriptado, clave

def desencriptador(encriptado, clave):
    clave_invertida = dict(zip(clave.values(), clave.keys()))
    desencriptado = ''
    for letter in list(encriptado):
        desencriptado += clave_invertida[letter]
        
    return desencriptado