#función que devuelve el total de una factura
def TotalFactura(bruto, iva):
    if iva == 0:
        total = bruto * 0.21 + bruto
    else:
        total = (bruto * iva)/100 +bruto
    return(total)


print (TotalFactura(1000, 35))
print (TotalFactura(1000, 0))