# Python String Methods - Cheatsheet para Testing

## Métodos de Validación de Contenido

### Verificar tipo de caracteres

```python
# .isalpha() - Solo letras
username = "Karina"
username.isalpha()  # True

username = "Karina123"
username.isalpha()  # False

# .isdigit() - Solo números
edad = "25"
edad.isdigit()  # True

edad = "25.5"
edad.isdigit()  # False

# .isalnum() - Letras y números (sin espacios ni símbolos)
password = "Pass123"
password.isalnum()  # True

password = "Pass 123"
password.isalnum()  # False (tiene espacio)

# .isspace() - Solo espacios en blanco
texto = "   "
texto.isspace()  # True
```

## Métodos de Búsqueda

### Verificar presencia de caracteres

```python
# in - Verificar si contiene algo
email = "karina@test.com"
"@" in email  # True
"." in email  # True

# .count() - Contar ocurrencias
password = "Pass123Pass"
password.count("Pass")  # 2
password.count("s")  # 2

# .find() - Encontrar posición (devuelve -1 si no encuentra)
email = "test@example.com"
email.find("@")  # 4
email.find("xyz")  # -1

# .index() - Similar a find() pero da error si no encuentra
email.index("@")  # 4
# email.index("xyz")  # ValueError
```

## Métodos de Validación de Formato

### Verificar inicio y fin

```python
# .startswith() - Comienza con
url = "https://www.google.com"
url.startswith("https")  # True
url.startswith("http")  # True

# .endswith() - Termina con
archivo = "datos.csv"
archivo.endswith(".csv")  # True
archivo.endswith(".txt")  # False
```

## Métodos de Transformación

### Cambiar mayúsculas/minúsculas

```python
texto = "Hola Mundo"

# .upper() - Todo mayúsculas
texto.upper()  # "HOLA MUNDO"

# .lower() - Todo minúsculas
texto.lower()  # "hola mundo"

# .capitalize() - Primera letra mayúscula
texto.capitalize()  # "Hola mundo"

# .title() - Primera letra de cada palabra
texto.title()  # "Hola Mundo"
```

### Limpiar espacios

```python
texto = "  Hola  "

# .strip() - Elimina espacios al inicio y final
texto.strip()  # "Hola"

# .lstrip() - Elimina espacios a la izquierda
texto.lstrip()  # "Hola  "

# .rstrip() - Elimina espacios a la derecha
texto.rstrip()  # "  Hola"
```

### Reemplazar contenido

```python
# .replace() - Reemplazar texto
texto = "Hola mundo mundo"
texto.replace("mundo", "Python")  # "Hola Python Python"
texto.replace("mundo", "Python", 1)  # "Hola Python mundo" (solo 1ra)
```

## Métodos de División y Unión

### Dividir strings

```python
# .split() - Dividir en lista
texto = "usuario,password,email"
datos = texto.split(",")  # ["usuario", "password", "email"]

texto = "Hola mundo Python"
palabras = texto.split()  # ["Hola", "mundo", "Python"] (espacio por defecto)

# .splitlines() - Dividir por líneas
texto = "Línea 1\nLínea 2\nLínea 3"
lineas = texto.splitlines()  # ["Línea 1", "Línea 2", "Línea 3"]
```

### Unir strings

```python
# .join() - Unir lista en string
lista = ["usuario", "password", "email"]
",".join(lista)  # "usuario,password,email"
" - ".join(lista)  # "usuario - password - email"
```

## Métodos de Longitud y Contenido

### Información del string

```python
texto = "Python Testing"

# len() - Longitud (función, no método)
len(texto)  # 14

# .count() - Contar caracteres específicos
texto.count("t")  # 2 (minúsculas)
texto.count("T")  # 1 (mayúsculas)
```

## Conversiones de Tipo

### Convertir desde/hacia strings

```python
# str() - Convertir a string
numero = 123
texto = str(numero)  # "123"

# int() - String a entero
texto = "123"
numero = int(texto)  # 123

# float() - String a decimal
texto = "123.45"
numero = float(texto)  # 123.45

# list() - String a lista de caracteres
texto = "Hola"
list(texto)  # ["H", "o", "l", "a"]
```

## Casos de Uso Comunes en Testing

### Validación de Email

```python
email = input("Email: ")

# Verificar @ y punto
if "@" in email and "." in email:
    # Verificar que @ viene antes del punto
    pos_arroba = email.index("@")
    pos_punto = email.index(".")
    if pos_arroba < pos_punto:
        print("Email válido")
```

### Validación de Password

```python
password = input("Password: ")

# Verificar longitud
if len(password) >= 6:
    # Verificar que contiene números
    tiene_numero = False
    for char in password:
        if char.isdigit():
            tiene_numero = True
    
    if tiene_numero:
        print("Password válido")
```

### Validación de Username

```python
username = input("Username: ")

# Solo letras y números
if username.isalnum() and len(username) >= 3:
    print("Username válido")
```

### Limpiar datos de entrada

```python
# Eliminar espacios y convertir a minúsculas
username = input("Username: ").strip().lower()

# Normalizar email
email = input("Email: ").strip().lower()
```

## Combinaciones Útiles

### Validación completa de campo

```python
campo = input("Campo: ")

# Limpiar espacios
campo = campo.strip()

# Verificar no vacío
if campo:
    # Verificar longitud
    if len(campo) >= 3:
        # Verificar solo letras
        if campo.isalpha():
            print("Campo válido")
```

### Búsqueda case-insensitive

```python
texto = "Python Testing Framework"
buscar = "python"

if buscar.lower() in texto.lower():
    print("Encontrado")
```

## Tips para Testing

- Siempre usa `.strip()` en inputs del usuario
- Valida tipo antes de convertir con `int()` o `float()`
- Usa `.lower()` para comparaciones case-insensitive
- Combina validaciones para mayor robustez
- `in` es más rápido que `.find()` para verificar presencia
- `.isdigit()` no funciona con números negativos o decimales

## Recursos Adicionales

- Documentación oficial: https://docs.python.org/3/library/stdtypes.html#string-methods
- Para más métodos avanzados: revisar módulo `re` (regex) en semanas futuras