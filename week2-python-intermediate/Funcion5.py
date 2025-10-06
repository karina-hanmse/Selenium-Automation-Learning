# función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
def AreaCirculo(radio):
    area = 3.1416 *radio*radio
    return area

def VolCilindro(radio, altura):
    return AreaCirculo(radio)*altura

print (VolCilindro(8,6))

