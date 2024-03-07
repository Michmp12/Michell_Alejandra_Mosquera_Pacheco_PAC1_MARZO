productos_por_categoria = {
   "Ferretería": 0,
   "Aseo": 0,
   "Seguridad": 0,
   "Alimentos": 0,
   "Electrodomésticos": 0
}

descuentos = {
   "Ferretería": 0.1,
   "Aseo": 0.05,
   "Seguridad": 0.15,
   "Alimentos": 0.08,
   "Electrodomésticos": 0.12
}

total_precio = 0

while True:
   categoriaInt = input("Ingrese la categoría del producto (Ferretería, Aseo, Seguridad, Alimentos, Electrodomésticos) o 'TERMINAR' para finalizar: ").capitalize()

   if categoriaInt == "Terminar":
       break

   if categoriaInt not in productos_por_categoria:
       print("Categoría inválida. Inténtelo nuevamente.")
       continue

   precio = float(input("Ingrese el precio del producto: "))

   descuento = descuentos[categoriaInt]
   precio_con_descuento = precio - (precio * descuento)

   productos_por_categoria[categoriaInt] += 1
   total_precio += precio_con_descuento

   print(f"El precio final con descuento es: {precio_con_descuento:.2f}")

print("\nResumen de Ventas:")
for categoriaInt, cantidad in productos_por_categoria.items():
   print(f"Cantidad de productos de {categoriaInt}: {cantidad}")

print(f"\nTotal para pagar: {total_precio:.2f}")