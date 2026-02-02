from modulos.datos_basicos import (
    capturar_producto_completo,
    formatear_producto,
    CATEGORIAS_DISPONIBLES
)
from modulos.validaciones import (
    validar_id_producto,
    validar_texto_no_vacio,
    validar_numero_positivo,
    validar_entero_positivo,
    validar_si_no
)

productos = []

nombres_productos = set()

contador_id = 1

def agregar_producto():
    global contador_id, productos, nombres_productos
    
    nuevo_producto = capturar_producto_completo(contador_id)
    
    if nuevo_producto is None:
        print("\n⚠️ Operación cancelada.")
        return
    
    nombre_lower = nuevo_producto['nombre'].lower()
    
    if nombre_lower in nombres_productos:
        print(f"\n⚠️ Advertencia: Ya existe un producto con el nombre '{nuevo_producto['nombre']}'.")
        confirmacion = input("¿Desea agregarlo de todas formas? (s/n): ")
        
        respuesta = validar_si_no(confirmacion)
        if respuesta is False or respuesta is None:
            print("\n⚠️ Producto no agregado.")
            return
    
    productos.append(nuevo_producto)
    
    nombres_productos.add(nombre_lower)
    
    contador_id += 1
    
    print(f"\n✅ Producto agregado exitosamente con ID {nuevo_producto['id']}!")

def listar_productos():
    if not productos:
        print("\n📭 No hay productos en el inventario.")
        return
    
    print("\n" + "=" * 100)
    print("📋 LISTADO DE PRODUCTOS")
    print("=" * 100)
    print(f"{'ID':<5} {'Nombre':<20} {'Precio':<12} {'Stock':<8} {'Categoría':<15} {'Valor Total':<15}")
    print("-" * 100)
    
    for producto in productos:
        print(
            f"{producto['id']:<5} "
            f"{producto['nombre']:<20} "
            f"${producto['precio']:<11.2f} "
            f"{producto['cantidad']:<8} "
            f"{producto['categoria']:<15} "
            f"${producto['valor_total']:<14.2f}"
        )
    
    print("=" * 100)
    print(f"Total de productos: {len(productos)}")

def buscar_producto_por_nombre():
    if not productos:
        print("\n📭 No hay productos en el inventario.")
        return
    
    print("\n🔍 Ingrese el nombre del producto a buscar:")
    nombre_buscar = input("➤ ").strip().lower()
    
    if not nombre_buscar:
        print("❌ Debe ingresar un nombre para buscar.")
        return
    
    productos_encontrados = []
    
    for producto in productos:
        if nombre_buscar in producto['nombre'].lower():
            productos_encontrados.append(producto)
    
    if productos_encontrados:
        print(f"\n✅ Se encontraron {len(productos_encontrados)} producto(s):")
        print("-" * 100)
        
        for producto in productos_encontrados:
            print(formatear_producto(producto))
        
        print("-" * 100)
    else:
        print(f"\n❌ No se encontraron productos con el nombre '{nombre_buscar}'.")

def buscar_producto_por_id():
    if not productos:
        print("\n📭 No hay productos en el inventario.")
        return None
    
    print("\n🔍 Ingrese el ID del producto a buscar:")
    id_input = input("➤ ").strip()
    
    id_validado = validar_id_producto(id_input, productos)
    
    if id_validado is None:
        return None
    
    for producto in productos:
        if producto['id'] == id_validado:
            print("\n✅ Producto encontrado:")
            print("-" * 100)
            print(formatear_producto(producto))
            print("-" * 100)
            return producto
    
    return None

def modificar_producto():
    if not productos:
        print("\n📭 No hay productos en el inventario.")
        return
    
    print("\n✏️ MODIFICAR PRODUCTO")
    print("=" * 50)
    
    producto = buscar_producto_por_id()
    
    if producto is None:
        return
    
    while True:
        print("\n¿Qué desea modificar?")
        print("1. Nombre")
        print("2. Precio")
        print("3. Cantidad")
        print("4. Categoría")
        print("5. Terminar modificación")
        
        opcion = input("➤ ").strip()
        
        if opcion == '1':
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nombre_validado = validar_texto_no_vacio(nuevo_nombre, "nombre", min_longitud=3)
            
            if nombre_validado:
                nombres_productos.discard(producto['nombre'].lower())
                producto['nombre'] = nombre_validado.title()
                nombres_productos.add(producto['nombre'].lower())
                print("✅ Nombre actualizado.")
        
        elif opcion == '2':
            nuevo_precio = input("Nuevo precio: $").strip()
            precio_validado = validar_numero_positivo(nuevo_precio, "precio")
            
            if precio_validado is not None:
                producto['precio'] = round(precio_validado, 2)
                producto['valor_total'] = producto['precio'] * producto['cantidad']
                print("✅ Precio actualizado.")
        
        elif opcion == '3':
            nueva_cantidad = input("Nueva cantidad: ").strip()
            cantidad_validada = validar_entero_positivo(nueva_cantidad, "cantidad")
            
            if cantidad_validada is not None:
                producto['cantidad'] = cantidad_validada
                producto['valor_total'] = producto['precio'] * producto['cantidad']
                print("✅ Cantidad actualizada.")
        
        elif opcion == '4':
            from modulos.datos_basicos import capturar_categoria_producto
            nueva_categoria = capturar_categoria_producto()
            
            if nueva_categoria:
                producto['categoria'] = nueva_categoria
                print("✅ Categoría actualizada.")
        
        elif opcion == '5':
            print("\n✅ Modificación completada.")
            print(formatear_producto(producto))
            break
        
        else:
            print("❌ Opción inválida.")

def eliminar_producto():
    global productos, nombres_productos
    
    if not productos:
        print("\n📭 No hay productos en el inventario.")
        return
    
    print("\n🗑️ ELIMINAR PRODUCTO")
    print("=" * 50)
    
    producto = buscar_producto_por_id()
    
    if producto is None:
        return
    
    print(f"\n⚠️ ¿Está seguro de eliminar el producto '{producto['nombre']}'?")
    confirmacion = input("Esta acción no se puede deshacer (s/n): ")
    
    respuesta = validar_si_no(confirmacion)
    
    if respuesta is True:
        nombres_productos.discard(producto['nombre'].lower())
        
        productos.remove(producto)
        
        print(f"\n✅ Producto '{producto['nombre']}' eliminado exitosamente.")
    else:
        print("\n⚠️ Eliminación cancelada.")

def listar_por_categoria():
    if not productos:
        print("\n📭 No hay productos en el inventario.")
        return
    
    from modulos.datos_basicos import mostrar_categorias, capturar_categoria_producto
    
    categoria_seleccionada = capturar_categoria_producto()
    
    if categoria_seleccionada is None:
        return
    
    productos_categoria = [p for p in productos if p['categoria'] == categoria_seleccionada]
    
    if productos_categoria:
        print(f"\n📂 Productos en la categoría '{categoria_seleccionada}':")
        print("-" * 100)
        
        for producto in productos_categoria:
            print(formatear_producto(producto))
        
        print("-" * 100)
        print(f"Total: {len(productos_categoria)} producto(s)")
    else:
        print(f"\n📭 No hay productos en la categoría '{categoria_seleccionada}'.")

def obtener_productos_bajo_stock(minimo=5):
    return [p for p in productos if p['cantidad'] < minimo]

if __name__ == "__main__":
    print("=== Prueba del Módulo de Gestión de Datos ===\n")
    
    print("Agregando productos de prueba...")
    
    productos_prueba = [
        {'id': 1, 'nombre': 'Laptop HP', 'precio': 850.00, 'cantidad': 10, 'categoria': 'Electrónica', 'valor_total': 8500.00},
        {'id': 2, 'nombre': 'Mouse Logitech', 'precio': 25.50, 'cantidad': 50, 'categoria': 'Electrónica', 'valor_total': 1275.00},
        {'id': 3, 'nombre': 'Camiseta Nike', 'precio': 35.00, 'cantidad': 20, 'categoria': 'Ropa', 'valor_total': 700.00}
    ]
    
    productos.extend(productos_prueba)
    contador_id = 4
    
    for p in productos_prueba:
        nombres_productos.add(p['nombre'].lower())
    
    listar_productos()