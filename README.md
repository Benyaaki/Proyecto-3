# Sistema de Gestión de Productos - Módulo 3 Python

Sistema de gestión de inventario desarrollado en Python con dos versiones: terminal y web.

## 📋 Descripción

Proyecto final del Módulo 3 de Python que implementa un sistema completo de gestión de productos con las siguientes características:

- **Versión Terminal**: Interfaz de línea de comandos interactiva
- **Versión Web**: Aplicación web moderna con Flask y diseño profesional

## ✨ Características

- ✅ CRUD completo de productos (Crear, Leer, Actualizar, Eliminar)
- ✅ Búsqueda por nombre o ID
- ✅ Filtrado por categorías
- ✅ Estadísticas del inventario en tiempo real
- ✅ Validaciones robustas de datos
- ✅ Interfaz web responsive con tema oscuro
- ✅ API REST completa

## 🚀 Instalación

### Requisitos

- Python 3.7 o superior

### Versión Terminal

```bash
python main.py
```

No requiere dependencias adicionales.

### Versión Web

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar servidor:
```bash
python app.py
```

3. Abrir navegador en: `http://localhost:5000`

## 📁 Estructura del Proyecto

```
Proyecto Modulo 3/
├── Documentacion/
│   ├── README.txt
│   └── ESTRUCTURA.txt
├── modulos/
│   ├── __init__.py
│   ├── datos_basicos.py
│   ├── validaciones.py
│   ├── gestion_datos.py
│   ├── funciones_utiles.py
│   └── menu.py
├── static/
│   ├── index.html
│   ├── css/style.css
│   └── js/app.js
├── main.py
├── app.py
└── requirements.txt
```

## 🛠️ Tecnologías Utilizadas

### Backend
- Python 3.7+
- Flask 3.1.2
- Flask-CORS 4.0.0

### Frontend
- HTML5
- CSS3 (Vanilla)
- JavaScript ES6+

## 📚 Conceptos de Python Aplicados

- Estructuras de datos: listas, diccionarios, tuplas, sets
- Control de flujo: if/elif/else, while, for, break, continue
- Funciones con parámetros y return
- Funciones recursivas
- Manejo de errores con try/except
- Modularización del código
- Validaciones de entrada

## 🎨 Diseño

La interfaz web cuenta con:
- Tema oscuro profesional
- Gradientes azul/morado
- Iconos SVG monocromos
- Efectos glassmorphism
- Diseño responsive

## 📝 Funcionalidades

### Versión Terminal
1. Agregar productos
2. Listar todos los productos
3. Buscar productos
4. Modificar productos
5. Eliminar productos
6. Ver por categoría
7. Ver estadísticas
8. Alertas de stock bajo

### Versión Web
- Dashboard con estadísticas en tiempo real
- Tabla interactiva de productos
- Búsqueda instantánea
- Modales para agregar/editar
- Confirmaciones de eliminación
- Notificaciones toast

## 🔗 API Endpoints

```
GET    /api/productos          - Lista todos los productos
POST   /api/productos          - Crea un producto nuevo
GET    /api/productos/<id>     - Obtiene un producto específico
PUT    /api/productos/<id>     - Actualiza un producto
DELETE /api/productos/<id>     - Elimina un producto
GET    /api/estadisticas       - Obtiene estadísticas
GET    /api/categorias         - Lista categorías disponibles
```

## 📄 Licencia

Proyecto académico - Módulo 3 Python

## 👤 Autor

Desarrollado como proyecto final del Módulo 3 de Python
