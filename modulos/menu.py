from modulos.gestion_datos import (
    agregar_producto,
    listar_productos,
    buscar_producto_por_nombre,
    buscar_producto_por_id,
    modificar_producto,
    eliminar_producto,
    listar_por_categoria,
    obtener_productos_bajo_stock,
    productos
)
from modulos.funciones_utiles import mostrar_estadisticas
from modulos.validaciones import validar_opcion_menu

def mostrar_banner():
    print("\n" + "=" * 80)
    print("🛒 SISTEMA DE GESTIÓN DE PRODUCTOS".center(80))
    print("Módulo 3 - Fundamentos de Python".center(80))
    print("=" * 80)

def mostrar_menu_principal():
    print("\n" + "─" * 80)
    print("📋 MENÚ PRINCIPAL")
    print("─" * 80)
    print("1️⃣  Agregar producto")
    print("2️⃣  Listar todos los productos")
    print("3️⃣  Buscar producto por nombre")
    print("4️⃣  Buscar producto por ID")
    print("5️⃣  Modificar producto")
    print("6️⃣  Eliminar producto")
    print("7️⃣  Listar productos por categoría")
    print("8️⃣  Ver estadísticas del inventario")
    print("9️⃣  Ver productos con stock bajo")
    print("0️⃣  Salir del sistema")
    print("─" * 80)

def mostrar_productos_bajo_stock():
    print("\n⚠️ PRODUCTOS CON STOCK BAJO")
    print("=" * 80)
    
    print("Ingrese el stock mínimo para la alerta (por defecto 10):")
    minimo_input = input("➤ ").strip()
    
    if minimo_input:
        try:
            minimo = int(minimo_input)
        except ValueError:
            print("❌ Valor inválido, usando 10 por defecto.")
            minimo = 10
    else:
        minimo = 10
    
    productos_bajo_stock = obtener_productos_bajo_stock(minimo)
    
    if productos_bajo_stock:
        print(f"\n⚠️ Hay {len(productos_bajo_stock)} producto(s) con menos de {minimo} unidades:")
        print("-" * 80)
        
        for producto in productos_bajo_stock:
            print(
                f"ID: {producto['id']:03d} | "
                f"{producto['nombre']:20s} | "
                f"Stock: {producto['cantidad']:4d} unidades | "
                f"Categoría: {producto['categoria']}"
            )
        
        print("-" * 80)
    else:
        print(f"\n✅ No hay productos con stock menor a {minimo} unidades.")

def pausar():
    input("\nPresione Enter para continuar...")

def ejecutar_menu():
    mostrar_banner()
    
    while True:
        mostrar_menu_principal()
        
        opcion = input("\n➤ Seleccione una opción: ").strip()
        
        opciones_validas = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        opcion_validada = validar_opcion_menu(opcion, opciones_validas)
        
        if opcion_validada is None:
            pausar()
            continue
        
        if opcion_validada == '0':
            print("\n" + "=" * 80)
            print("👋 ¡Gracias por usar el Sistema de Gestión de Productos!")
            print("=" * 80)
            break
        
        elif opcion_validada == '1':
            agregar_producto()
            pausar()
        
        elif opcion_validada == '2':
            listar_productos()
            pausar()
        
        elif opcion_validada == '3':
            buscar_producto_por_nombre()
            pausar()
        
        elif opcion_validada == '4':
            buscar_producto_por_id()
            pausar()
        
        elif opcion_validada == '5':
            modificar_producto()
            pausar()
        
        elif opcion_validada == '6':
            eliminar_producto()
            pausar()
        
        elif opcion_validada == '7':
            listar_por_categoria()
            pausar()
        
        elif opcion_validada == '8':
            mostrar_estadisticas(productos)
            pausar()
        
        elif opcion_validada == '9':
            mostrar_productos_bajo_stock()
            pausar()

if __name__ == "__main__":
    print("=== Prueba del Módulo de Menú ===\n")
    ejecutar_menu()