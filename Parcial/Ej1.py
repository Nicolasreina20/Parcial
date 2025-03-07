monto_compra = float(input("Ingrese el monto de la compra: "))
if monto_compra < 50:
    descuento = 0
elif monto_compra >= 50 and monto_compra <= 100 :
    descuento = 0.05
elif monto_compra >100:
    descuento = 0.10
descuento_aplicado = monto_compra * descuento
monto_final = monto_compra - descuento_aplicado
print("Descuento $",descuento_aplicado)
print("Monto a pagar $",monto_final)
