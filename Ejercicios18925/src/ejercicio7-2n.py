frase = input("Introduce una frase\n")
caracteres = len(frase)
lista = frase.split()
numero_palabras = len(lista)
palabra_larga = ""
for palabra in lista:
    if(len(palabra)>len(palabra_larga)):
        palabra_larga = palabra

print(f"Número de caracteres: {caracteres}")
print((f"Número de palabras: {numero_palabras}"))
print((f"Plabra más larga: {palabra_larga}"))