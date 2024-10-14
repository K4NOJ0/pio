# Lista de productos disponibles
productos = [
    {"nombre": "Anillo de Oro", "precio": 500, "cantidad": 10},
    {"nombre": "Collar de Plata", "precio": 200, "cantidad": 5},
    {"nombre": "Reloj de Lujo", "precio": 1000, "cantidad": 3},
    {"nombre": "Pendientes de Diamante", "precio": 1500, "cantidad": 2}
]

# Carrito de compras
carrito = []

# Función para mostrar los productos disponibles
def mostrar_productos():
    print("\nProductos disponibles:")
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto['nombre']} - ${producto['precio']} (Stock: {producto['cantidad']})")

# Función para agregar productos al carrito
def agregar_al_carrito():
    mostrar_productos()
    try:
        seleccion = int(input("\nSelecciona el número del producto que deseas comprar: ")) - 1
        if seleccion < 0 or seleccion >= len(productos):
            print("Producto no válido.")
            return

        cantidad = int(input(f"¿Cuántas unidades de {productos[seleccion]['nombre']} deseas comprar?: "))
        if cantidad > productos[seleccion]["cantidad"]:
            print("No hay suficiente stock.")
        else:
            carrito.append({"nombre": productos[seleccion]["nombre"], "precio": productos[seleccion]["precio"], "cantidad": cantidad})
            productos[seleccion]["cantidad"] -= cantidad
            print(f"Se han añadido {cantidad} unidades de {productos[seleccion]['nombre']} al carrito.")
    except ValueError:
        print("Entrada no válida, intenta nuevamente.")

# Función para mostrar el carrito de compras
def mostrar_carrito():
    if not carrito:
        print("\nEl carrito está vacío.")
    else:
        print("\nCarrito de compras:")
        for item in carrito:
            print(f"{item['nombre']} - ${item['precio']} x {item['cantidad']}")

# Función para calcular el total de la compra
def calcular_total():
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return total

# Función para finalizar la compra
def finalizar_compra():
    if not carrito:
        print("\nEl carrito está vacío. No se puede finalizar la compra.")
        return

    mostrar_carrito()
    total = calcular_total()
    print(f"\nEl total a pagar es: ${total}")
    confirmacion = input("¿Deseas finalizar la compra? (s/n): ").lower()

    if confirmacion == 's':
        carrito.clear()
        print("\nCompra finalizada. ¡Gracias por tu compra!")
    else:
        print("\nCompra cancelada.")

# Función principal del menú
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Mostrar productos")
        print("2. Agregar producto al carrito")
        print("3. Mostrar carrito")
        print("4. Finalizar compra")
        print("5. Calcular Total")
        print("6. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            mostrar_productos()
        elif opcion == '2':
            agregar_al_carrito()
        elif opcion == '3':
            mostrar_carrito()
        elif opcion == '4':
            finalizar_compra()
        elif opcion == '5':
            mostrar_carrito()
            total = calcular_total()
            print(f"\nEl total a pagar es: ${total}")
        elif opcion == '6':
            print("Gracias por usar el sistema de ventas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor selecciona una opción correcta.")

# Ejecutar el programa
menu_principal()
