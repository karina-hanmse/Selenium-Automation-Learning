#Utilización de If
x = int(input("Ingrese un entero:"))
if x<0:
    x=0
    print ("Negativo cambia por Cero")
elif x==0:
    print("Zero")
elif x==1:
    print("Single")
else: 
    print("More")