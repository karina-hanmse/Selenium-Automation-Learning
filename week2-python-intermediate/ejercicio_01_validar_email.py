# ejercicio_01_validar_email.py
# Ejercicio: Validar formato de email
# Aprendizaje: Funciones con validaciones múltiples

def validar_email(email):
    """
    Valida si un email tiene formato correcto.
    
    Requisitos:
    - Debe contener exactamente un @
    - Debe tener al menos un punto después del @
    - No puede estar vacío
    - No puede tener espacios
    
    Parámetros:
    - email: string con el email a validar
    
    Retorna: True si es válido, False si no
    """
    if email is None:
        return False
    if " " in email:
        return False
    if email.count("@") != 1:
        return False
    # Dividir el email por @
    partes = email.split("@")

        # partes[0] = lo que va antes del @
        # partes[1] = lo que va después del @

        # Verificar que haya contenido antes y después del @
    if not partes[0] or not partes[1]:
        return False

    # Verificar si hay punto DESPUÉS del @
    if "." not in partes[1]:
        return False  # No hay punto en la parte después del @
   
    
    return True


# Casos de prueba (NO los borres, úsalos para verificar)
print("=== PRUEBAS DE VALIDACIÓN DE EMAIL ===")
print(validar_email("test@test.com"))           # Debe dar True
print(validar_email("karina@gmail.com"))        # Debe dar True
print(validar_email("test@testcom"))            # Debe dar False (falta punto)
print(validar_email("testtest.com"))            # Debe dar False (falta @)
print(validar_email(""))                        # Debe dar False (vacío)
print(validar_email("test @test.com"))          # Debe dar False (tiene espacio)
print(validar_email("test@@test.com"))          # Debe dar False (dos @)

print("\n=== CASOS EXTRA ===")
print(validar_email("@test.com"))               # False (falta parte antes del @)
print(validar_email("test@"))                   # False (falta parte después del @)
print(validar_email(None))                      # False (None)