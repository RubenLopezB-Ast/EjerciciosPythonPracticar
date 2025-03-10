#Escribe un programa que almacene un número y pida al usuario adivinarlo numeros del 1 al 10.
class adivinanza:
    numero_secreto = 2
    adivinanza = int(input("¿Que número estoy pensando: "))
    if adivinanza == numero_secreto:
        print("¡Eres un genio es este !")
    else:
        print("Prueba otra vez")

