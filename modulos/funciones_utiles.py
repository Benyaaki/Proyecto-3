from modulos.datos_basicos import CATEGORIAS_DISPONIBLES

def generar_id(productos):
    if not productos:
        return 1
    
    ids_existentes = [p['id'] for p in productos]
    return max(ids_existentes) + 1

def formatear_precio(precio):
    return f"${precio:,.2f}"

def formatear_cantidad(cantidad):
    return f"{cantidad:,}"

def calcular_valor_total_inventario(productos):
    if not productos:
        return 0.0
    
    total = sum(producto['valor_total'] for producto in productos)
    return round(total, 2)

def calcular_cantidad_total_productos(productos):
    if not productos:
        return 0
    
    return sum(producto['cantidad'] for producto in productos)

def calcular_precio_promedio(productos):
    if not productos:
        return 0.0
    
    total_precio = sum(producto['precio'] for producto in productos)
    return round(total_precio / len(productos), 2)

def contar_productos_por_categoria(productos):
    conteo = {}
    
    for categoria in CATEGORIAS_DISPONIBLES:
        conteo[categoria] = 0
    
    for producto in productos:
        if producto['categoria'] in conteo:
            conteo[producto['categoria']] += 1
    
    return conteo

def obtener_producto_mas_caro(productos):
    if not productos:
        return None
    
    return max(productos, key=lambda p: p['precio'])

def obtener_producto_mas_barato(productos):
    if not productos:
        return None
    
    return min(productos, key=lambda p: p['precio'])

def obtener_categoria_con_mas_productos(productos):
    if not productos:
        return (None, 0)
    
    conteo = contar_productos_por_categoria(productos)
    
    categoria_max = max(conteo.items(), key=lambda x: x[1])
    
    return categoria_max

def calcular_valor_por_categoria(productos):
    valores = {}
    
    for categoria in CATEGORIAS_DISPONIBLES:
        valores[categoria] = 0.0
    
    for producto in productos:
        if producto['categoria'] in valores:
            valores[producto['categoria']] += producto['valor_total']
    
    for categoria in valores:
        valores[categoria] = round(valores[categoria], 2)
    
    return valores

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursivo(n - 1)

def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def obtener_estadisticas_completas(productos):
    if not productos:
        return {
            'total_productos': 0,
            'total_unidades': 0,
            'valor_total': 0.0,
            'precio_promedio': 0.0,
            'producto_mas_caro': None,
            'producto_mas_barato': None,
            'productos_por_categoria': {},
            'valores_por_categoria': {},
            'categoria_principal': (None, 0)
        }
    
    return {
        'total_productos': len(productos),
        'total_unidades': calcular_cantidad_total_productos(productos),
        'valor_total': calcular_valor_total_inventario(productos),
        'precio_promedio': calcular_precio_promedio(productos),
        'producto_mas_caro': obtener_producto_mas_caro(productos),
        'producto_mas_barato': obtener_producto_mas_barato(productos),
        'productos_por_categoria': contar_productos_por_categoria(productos),
        'valores_por_categoria': calcular_valor_por_categoria(productos),
        'categoria_principal': obtener_categoria_con_mas_productos(productos)
    }

def mostrar_estadisticas(productos):
    stats = obtener_estadisticas_completas(productos)
    
    print("\n" + "=" * 80)
    print("📊 ESTADÍSTICAS DEL INVENTARIO")
    print("=" * 80)
    
    print(f"\n📦 Resumen General:")
    print(f"  • Total de productos diferentes: {stats['total_productos']}")
    print(f"  • Total de unidades en stock: {formatear_cantidad(stats['total_unidades'])}")
    print(f"  • Valor total del inventario: {formatear_precio(stats['valor_total'])}")
    print(f"  • Precio promedio por producto: {formatear_precio(stats['precio_promedio'])}")
    
    if stats['producto_mas_caro']:
        print(f"\n💎 Producto más caro:")
        print(f"  • {stats['producto_mas_caro']['nombre']} - {formatear_precio(stats['producto_mas_caro']['precio'])}")
    
    if stats['producto_mas_barato']:
        print(f"\n💰 Producto más barato:")
        print(f"  • {stats['producto_mas_barato']['nombre']} - {formatear_precio(stats['producto_mas_barato']['precio'])}")
    
    print(f"\n📂 Productos por categoría:")
    for categoria, cantidad in stats['productos_por_categoria'].items():
        if cantidad > 0:
            valor = stats['valores_por_categoria'][categoria]
            print(f"  • {categoria:15s}: {cantidad:3d} productos - {formatear_precio(valor)}")
    
    if stats['categoria_principal'][0]:
        print(f"\n🏆 Categoría principal:")
        print(f"  • {stats['categoria_principal'][0]} con {stats['categoria_principal'][1]} productos")
    
    print("=" * 80)

if __name__ == "__main__":
    print("=== Prueba del Módulo de Funciones Útiles ===\n")
    
    print("1. Factorial recursivo:")
    print(f"   5! = {factorial_recursivo(5)}")
    print(f"   10! = {factorial_recursivo(10)}")
    
    print("\n2. Fibonacci recursivo:")
    print(f"   Fibonacci(7) = {fibonacci_recursivo(7)}")
    print(f"   Fibonacci(10) = {fibonacci_recursivo(10)}")
    
    productos_prueba = [
        {'id': 1, 'nombre': 'Laptop HP', 'precio': 850.00, 'cantidad': 10, 'categoria': 'Electrónica', 'valor_total': 8500.00},
        {'id': 2, 'nombre': 'Mouse Logitech', 'precio': 25.50, 'cantidad': 50, 'categoria': 'Electrónica', 'valor_total': 1275.00},
        {'id': 3, 'nombre': 'Camiseta Nike', 'precio': 35.00, 'cantidad': 20, 'categoria': 'Ropa', 'valor_total': 700.00}
    ]
    
    print("\n3. Estadísticas del inventario:")
    mostrar_estadisticas(productos_prueba)