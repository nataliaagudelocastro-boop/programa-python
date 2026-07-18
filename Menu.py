# ----------------------------------------
# Matriz del menú del restaurante
# [Nombre, Categoría, Precio Base]
# ----------------------------------------

menu = [
    ["Hamburguesa", "Comida", 25000],
    ["Pizza", "Comida", 30000],
    ["Limonada", "Bebida", 9000],
    ["Café", "Bebida", 6000],
    ["Helado", "Postre", 12000],
    ["Brownie", "Postre", 15000]
]

# ----------------------------------------
# Configuración de la promoción
# ----------------------------------------

categoria_objetivo = "Comida"
umbral = 20000

# ----------------------------------------
# Función para calcular el precio final
# ----------------------------------------

def calcular_precio(categoria, precio):

    if categoria == categoria_objetivo and precio > umbral:
        descuento = precio * 0.15
        precio_final = precio - descuento
    else:
        precio_final = precio

    return precio_final

# ----------------------------------------
# Mostrar resultados
# ----------------------------------------

print("==============================================")
print("      PROMOCIÓN DEL RESTAURANTE")
print("==============================================")
print(f"Categoría en promoción: {categoria_objetivo}")
print(f"Descuento: 15%")
print(f"Aplica para precios mayores a: ${umbral}")
print("==============================================")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio = producto[2]

    precio_final = calcular_precio(categoria, precio)

    print("\nProducto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio)
    print("Precio Final: $", precio_final)
    print("----------------------------------------------")