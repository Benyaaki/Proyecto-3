def validar_numero_positivo(valor, nombre_campo="número"):
    try:
        numero = float(valor)
        
        if numero <= 0:
            print(f"❌ Error: El {nombre_campo} debe ser mayor que cero.")
            return None
        elif numero > 1000000:
            print(f"⚠️ Advertencia: El {nombre_campo} es muy alto ({numero})")
            confirmacion = input("¿Desea continuar? (s/n): ").lower()
            if confirmacion != 's':
                return None
        
        return numero
    
    except ValueError:
        print(f"❌ Error: '{valor}' no es un {nombre_campo} válido.")
        return None

def validar_entero_positivo(valor, nombre_campo="número"):
    try:
        numero = int(valor)
        
        if numero <= 0:
            print(f"❌ Error: El {nombre_campo} debe ser mayor que cero.")
            return None
        
        return numero
    
    except ValueError:
        print(f"❌ Error: '{valor}' no es un {nombre_campo} entero válido.")
        return None

def validar_texto_no_vacio(texto, nombre_campo="texto", min_longitud=1, max_longitud=100):
    texto_limpio = texto.strip()
    
    if not texto_limpio:
        print(f"❌ Error: El {nombre_campo} no puede estar vacío.")
        return None
    elif len(texto_limpio) < min_longitud:
        print(f"❌ Error: El {nombre_campo} debe tener al menos {min_longitud} caracteres.")
        return None
    elif len(texto_limpio) > max_longitud:
        print(f"❌ Error: El {nombre_campo} no puede exceder {max_longitud} caracteres.")
        return None
    elif texto_limpio.isdigit():
        print(f"❌ Error: El {nombre_campo} no puede ser solo números.")
        return None
    
    return texto_limpio

def validar_opcion_menu(opcion, opciones_validas):
    opcion_limpia = opcion.strip()
    
    if opcion_limpia in opciones_validas:
        return opcion_limpia
    else:
        print(f"❌ Error: Opción inválida. Opciones válidas: {', '.join(opciones_validas)}")
        return None

def validar_categoria(categoria, categorias_disponibles):
    categoria_limpia = categoria.strip().title()
    
    if categoria_limpia in categorias_disponibles:
        return categoria_limpia
    else:
        print(f"❌ Error: Categoría inválida.")
        print(f"Categorías disponibles: {', '.join(categorias_disponibles)}")
        return None

def validar_si_no(respuesta):
    respuesta_limpia = respuesta.strip().lower()
    
    if respuesta_limpia in ['s', 'si', 'sí']:
        return True
    elif respuesta_limpia in ['n', 'no']:
        return False
    else:
        print("❌ Error: Respuesta inválida. Ingrese 's' para sí o 'n' para no.")
        return None

def validar_id_producto(id_producto, productos):
    try:
        id_num = int(id_producto)
        
        for producto in productos:
            if producto['id'] == id_num:
                return id_num
        
        print(f"❌ Error: No existe un producto con ID {id_num}.")
        return None
    
    except ValueError:
        print(f"❌ Error: '{id_producto}' no es un ID válido.")
        return None

if __name__ == "__main__":
    print("=== Pruebas de Validaciones ===\n")
    
    print("1. Validar número positivo:")
    validar_numero_positivo("100", "precio")
    validar_numero_positivo("-50", "precio")
    validar_numero_positivo("abc", "precio")
    
    print("\n2. Validar texto no vacío:")
    validar_texto_no_vacio("Producto válido", "nombre")
    validar_texto_no_vacio("", "nombre")
    validar_texto_no_vacio("AB", "nombre", min_longitud=3)