from modulos.validaciones import (
    validar_numero_positivo,
    validar_entero_positivo,
    validar_texto_no_vacio,
    validar_categoria
)

CATEGORIAS_DISPONIBLES = (
    'Electrónica',
    'Ropa',
    'Alimentos',
    'Hogar',
    'Deportes',
    'Libros',
    'Juguetes',
    'Otros'
)

def mostrar_categorias():
    print("\n📂 Categorías disponibles:")
    print("=" * 40)
    
    for i, categoria in enumerate(CATEGORIAS_DISPONIBLES, start=1):
        print(f"  {i}. {categoria}")
    
    print("=" * 40)

def capturar_nombre_producto():
    while True:
        print("\n📝 Ingrese el nombre del producto (o 'cancelar' para volver):")
        nombre = input("➤ ").strip()
        
        if nombre.lower() == 'cancelar':
            return None
        
        nombre_validado = validar_texto_no_vacio(nombre, "nombre del producto", min_longitud=3)
        
        if nombre_validado:
            return nombre_validado.title()

def capturar_precio_producto():
    while True:
        print("\n💰 Ingrese el precio del producto (o 'cancelar' para volver):")
        precio_input = input("➤ $").strip()
        
        if precio_input.lower() == 'cancelar':
            return None
        
        precio_validado = validar_numero_positivo(precio_input, "precio")
        
        if precio_validado is not None:
            return round(precio_validado, 2)

def capturar_cantidad_producto():
    while True:
        print("\n📦 Ingrese la cantidad en stock (o 'cancelar' para volver):")
        cantidad_input = input("➤ ").strip()
        
        if cantidad_input.lower() == 'cancelar':
            return None
        
        cantidad_validada = validar_entero_positivo(cantidad_input, "cantidad")
        
        if cantidad_validada is not None:
            return cantidad_validada

def capturar_categoria_producto():
    mostrar_categorias()
    
    while True:
        print("\n🏷️ Seleccione el número de categoría (o 'cancelar' para volver):")
        categoria_input = input("➤ ").strip()
        
        if categoria_input.lower() == 'cancelar':
            return None
        
        try:
            indice = int(categoria_input)
            
            if 1 <= indice <= len(CATEGORIAS_DISPONIBLES):
                return CATEGORIAS_DISPONIBLES[indice - 1]
            else:
                print(f"❌ Error: Seleccione un número entre 1 y {len(CATEGORIAS_DISPONIBLES)}.")
        
        except ValueError:
            print("❌ Error: Ingrese un número válido.")

def capturar_producto_completo(id_producto):
    print("\n" + "=" * 50)
    print("🆕 AGREGAR NUEVO PRODUCTO")
    print("=" * 50)
    
    nombre = capturar_nombre_producto()
    if nombre is None:
        return None
    
    precio = capturar_precio_producto()
    if precio is None:
        return None
    
    cantidad = capturar_cantidad_producto()
    if cantidad is None:
        return None
    
    categoria = capturar_categoria_producto()
    if categoria is None:
        return None
    
    valor_total = precio * cantidad
    
    producto = {
        'id': id_producto,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad,
        'categoria': categoria,
        'valor_total': valor_total
    }
    
    print("\n" + "=" * 50)
    print("✅ RESUMEN DEL PRODUCTO")
    print("=" * 50)
    print(f"ID:            {producto['id']}")
    print(f"Nombre:        {producto['nombre']}")
    print(f"Precio:        ${producto['precio']:.2f}")
    print(f"Cantidad:      {producto['cantidad']} unidades")
    print(f"Categoría:     {producto['categoria']}")
    print(f"Valor Total:   ${producto['valor_total']:.2f}")
    print("=" * 50)
    
    return producto

def formatear_producto(producto):
    return (
        f"ID: {producto['id']:03d} | "
        f"{producto['nombre']:20s} | "
        f"${producto['precio']:8.2f} | "
        f"Stock: {producto['cantidad']:4d} | "
        f"Cat: {producto['categoria']:15s} | "
        f"Total: ${producto['valor_total']:10.2f}"
    )

if __name__ == "__main__":
    print("=== Prueba del Módulo de Datos Básicos ===\n")
    
    producto_prueba = capturar_producto_completo(1)
    
    if producto_prueba:
        print("\n✅ Producto capturado exitosamente:")
        print(formatear_producto(producto_prueba))