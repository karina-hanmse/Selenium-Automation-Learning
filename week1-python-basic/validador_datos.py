""""
Solicite al usuario estos datos:

Username (mínimo 3 caracteres, no vacío)
Password (mínimo 6 caracteres, debe contener números)
Email (debe contener @ y punto)
Edad (debe ser número entre 18 y 100)


Validar cada campo y muestre:

"VÁLIDO" si cumple los criterios
"INVÁLIDO" con razón específica si no cumple


Al final muestra un resumen:

Cantidad de campos válidos vs inválidos
Si todos son válidos: "Datos aptos para testing"
"""
print ("======== Validador de datos de pruebas =======")
#Solicitar datos
username = input("Ingrese username: ")
password = input("Ingrese contraseña: ")
email = input("Ingrese email:")
edad = input("Ingrese edad: ")

#contador de validos e invalidos
validos = 0
invalidos = 0
todos_validos = True
#validar username
if len(username)>= 3 and username.isalpha():
    print ("Username Válido")
    
else:
    print ("Usename Inválido - Mímimo 3 caracteres")
    todos_validos = False
    
if password.isdigit() and len(password )>= 6:
    print ("Password Válida")
else:
    print ("Password inválida")
    todos_validos = False


if "@" in email and "." in email:
    posicion_arroba = email.index("@")
    posicion_punto = email.index(".")
    
    if posicion_arroba < posicion_punto:
        print("Email: VÁLIDO")
    else:
        print("Email: INVÁLIDO - formato incorrecto")
        todos_validos = False
else:
    print("Email: INVÁLIDO - falta @ o punto")

if edad.isdigit():
    edad_numero = int(edad)
    if edad_numero >= 18 and edad_numero <= 100:
        print("Edad: VÁLIDA")
        
    else:
        print("Edad: INVÁLIDA - debe estar entre 18 y 100")
        todos_validos = False
else:
    print("Edad: INVÁLIDA - debe ser un número")
    todos_validos= False

if todos_validos:
    print("Todos los datos son válidos - Aptos para testing")
    validos = validos + 1
    print ("Cantidad de datos válidos:", validos)
else:
    print("Hay datos inválidos - No aptos para testing")
    invalidos = invalidos +1
    print ("Cantidad de datos invalidos:", invalidos)