def solucion(b,n):
    cantidad_intentada = 0
    i = True

    numero = int(input("Numero a ingresar para adivinar: "))
    cantidad_intentada = cantidad_intentada + 1

    while i:
        if(n < numero) and (numero <= b and numero>-1):
           print("¡Ups! Te pasaste")
           numero = int(input("numero a ingresar para adivinar: "))
           cantidad_intentada = cantidad_intentada + 1
        elif (n == numero ) and (numero <= b and numero>-1):
           print(f"¡LO LOGRASTE! Usaste {cantidad_intentada} intentos")
           i = False
        elif (n > numero) and (numero <= b and numero>-1):
           print("¡Ups! Estás por debajo")
           numero = int(input("numero a ingresar para adivinar: "))
           cantidad_intentada = cantidad_intentada + 1
        else:  
           print("¡Te saliste del intervalo!")  
           numero = int(input("numero a ingresar para adivinar: "))