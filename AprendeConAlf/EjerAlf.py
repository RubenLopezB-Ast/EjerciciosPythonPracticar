"""Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!."""
print("¡HoLa Mundo!")

"""Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el
contenido de la variable."""
saludo = "¡Hola Mundo!"
print(saludo)

"""Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo
introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario
haya introducido."""
name = input("¿Cuál es tu nombre amigo?")
print("¡Hola " + name + "!")

"""Ejercicio 4
 Escribir un programa que muestre por pantalla el resultado de la siguiente operación
aritmética (3+2/2X5) al cuadrado."""
print(((3+2)/(2*5))**2)

"""Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde."""

hour_work = float(input("¿Cuantas horas hás estado en tu lugar de trabajo? "))
price_hour = float(input("¿A cuantos euros se te paga por hora trabajada?"))
total_euro = hour_work*price_hour
print("Por " , hour_work , " trabajadas cobrarás " , total_euro , " euros.")
