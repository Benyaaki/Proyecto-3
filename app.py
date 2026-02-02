from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

from modulos.gestion_datos import (
    productos,
    nombres_productos,
    contador_id,
    agregar_producto as agregar_producto_terminal
)
from modulos.datos_basicos import CATEGORIAS_DISPONIBLES
from modulos.funciones_utiles import obtener_estadisticas_completas
from modulos.validaciones import (
    validar_numero_positivo,
    validar_entero_positivo,
    validar_texto_no_vacio,
    validar_categoria
)

app = Flask(__name__, static_folder='static')
CORS(app)

_contador_id = 1


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    return jsonify({
        'success': True,
        'productos': productos,
        'total': len(productos)
    })


@app.route('/api/productos/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    
    if producto:
        return jsonify({
            'success': True,
            'producto': producto
        })
    else:
        return jsonify({
            'success': False,
            'error': f'Producto con ID {producto_id} no encontrado'
        }), 404


@app.route('/api/productos', methods=['POST'])
def crear_producto():
    global _contador_id
    
    try:
        data = request.get_json()
        
        nombre = validar_texto_no_vacio(data.get('nombre', ''), 'nombre', min_longitud=3)
        if nombre is None:
            return jsonify({'success': False, 'error': 'Nombre inválido'}), 400
        
        precio = validar_numero_positivo(str(data.get('precio', 0)), 'precio')
        if precio is None:
            return jsonify({'success': False, 'error': 'Precio inválido'}), 400
        
        cantidad = validar_entero_positivo(str(data.get('cantidad', 0)), 'cantidad')
        if cantidad is None:
            return jsonify({'success': False, 'error': 'Cantidad inválida'}), 400
        
        categoria = validar_categoria(data.get('categoria', ''), CATEGORIAS_DISPONIBLES)
        if categoria is None:
            return jsonify({'success': False, 'error': 'Categoría inválida'}), 400
        
        nombre_lower = nombre.lower()
        if nombre_lower in nombres_productos:
            return jsonify({
                'success': False,
                'error': f'Ya existe un producto con el nombre "{nombre}"'
            }), 400
        
        nuevo_producto = {
            'id': _contador_id,
            'nombre': nombre.title(),
            'precio': round(precio, 2),
            'cantidad': cantidad,
            'categoria': categoria,
            'valor_total': round(precio * cantidad, 2)
        }
        
        productos.append(nuevo_producto)
        nombres_productos.add(nombre_lower)
        _contador_id += 1
        
        return jsonify({
            'success': True,
            'producto': nuevo_producto,
            'message': 'Producto creado exitosamente'
        }), 201
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    try:
        producto = next((p for p in productos if p['id'] == producto_id), None)
        
        if not producto:
            return jsonify({
                'success': False,
                'error': f'Producto con ID {producto_id} no encontrado'
            }), 404
        
        data = request.get_json()
        
        if 'nombre' in data:
            nombre = validar_texto_no_vacio(data['nombre'], 'nombre', min_longitud=3)
            if nombre is None:
                return jsonify({'success': False, 'error': 'Nombre inválido'}), 400
            
            nombres_productos.discard(producto['nombre'].lower())
            producto['nombre'] = nombre.title()
            nombres_productos.add(producto['nombre'].lower())
        
        if 'precio' in data:
            precio = validar_numero_positivo(str(data['precio']), 'precio')
            if precio is None:
                return jsonify({'success': False, 'error': 'Precio inválido'}), 400
            producto['precio'] = round(precio, 2)
        
        if 'cantidad' in data:
            cantidad = validar_entero_positivo(str(data['cantidad']), 'cantidad')
            if cantidad is None:
                return jsonify({'success': False, 'error': 'Cantidad inválida'}), 400
            producto['cantidad'] = cantidad
        
        if 'categoria' in data:
            categoria = validar_categoria(data['categoria'], CATEGORIAS_DISPONIBLES)
            if categoria is None:
                return jsonify({'success': False, 'error': 'Categoría inválida'}), 400
            producto['categoria'] = categoria
        
        producto['valor_total'] = round(producto['precio'] * producto['cantidad'], 2)
        
        return jsonify({
            'success': True,
            'producto': producto,
            'message': 'Producto actualizado exitosamente'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    try:
        producto = next((p for p in productos if p['id'] == producto_id), None)
        
        if not producto:
            return jsonify({
                'success': False,
                'error': f'Producto con ID {producto_id} no encontrado'
            }), 404
        
        nombres_productos.discard(producto['nombre'].lower())
        productos.remove(producto)
        
        return jsonify({
            'success': True,
            'message': f'Producto "{producto["nombre"]}" eliminado exitosamente'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/estadisticas', methods=['GET'])
def obtener_estadisticas():
    try:
        stats = obtener_estadisticas_completas(productos)
        
        if stats['producto_mas_caro']:
            stats['producto_mas_caro'] = {
                'id': stats['producto_mas_caro']['id'],
                'nombre': stats['producto_mas_caro']['nombre'],
                'precio': stats['producto_mas_caro']['precio']
            }
        
        if stats['producto_mas_barato']:
            stats['producto_mas_barato'] = {
                'id': stats['producto_mas_barato']['id'],
                'nombre': stats['producto_mas_barato']['nombre'],
                'precio': stats['producto_mas_barato']['precio']
            }
        
        return jsonify({
            'success': True,
            'estadisticas': stats
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/categorias', methods=['GET'])
def obtener_categorias():
    return jsonify({
        'success': True,
        'categorias': list(CATEGORIAS_DISPONIBLES)
    })


if __name__ == '__main__':
    print("\n" + "=" * 80)
    print("SERVIDOR WEB - SISTEMA DE GESTION DE PRODUCTOS")
    print("=" * 80)
    print("\nServidor iniciado en: http://localhost:5000")
    print("API REST disponible en: http://localhost:5000/api/")
    print("\nEndpoints disponibles:")
    print("   GET    /api/productos          - Listar productos")
    print("   POST   /api/productos          - Crear producto")
    print("   GET    /api/productos/<id>     - Obtener producto")
    print("   PUT    /api/productos/<id>     - Actualizar producto")
    print("   DELETE /api/productos/<id>     - Eliminar producto")
    print("   GET    /api/estadisticas       - Obtener estadísticas")
    print("   GET    /api/categorias         - Listar categorías")
    print("\n" + "=" * 80)
    print("Presiona Ctrl+C para detener el servidor\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
