import random
elementos = ("963214-addanilujhvyjyg")
pass_lenght = int(input("Introduzca la longitud de su contraseña: "))

pasword = ""
for i in range (pass_length):
    password += random.choice(elementos) # Se concatena el caracter a la variable "pasword"

print ("Contraseña generada:", password)S