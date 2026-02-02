Sistema de Gestion de Productos - Modulo 3
===========================================

Este es mi proyecto final del modulo 3 de Python. La idea era hacer un sistema
para manejar inventario de productos, y termine haciendo dos versiones: una para
la terminal y otra con interfaz web.


Que hace
--------

El sistema permite gestionar productos de un inventario. Puedes agregar productos
nuevos, ver los que ya tienes, buscar por nombre o ID, modificar datos y eliminar
los que no necesites mas.

Tambien calcula algunas estadisticas utiles como el valor total del inventario,
cantidad de productos, precio promedio, etc.

Hice dos versiones:
- Terminal: la version basica que pedia el modulo
- Web: le agregue despues una interfaz grafica porque queria practicar Flask


Como usarlo
-----------

VERSION TERMINAL:

Solo tienes que correr:
    python main.py

Te aparece un menu con varias opciones. Puedes agregar productos (te pide nombre,
precio, cantidad y categoria), ver la lista completa, buscar alguno especifico,
modificar datos, eliminar, filtrar por categoria, ver estadisticas y ver cuales
tienen stock bajo.


VERSION WEB:

Primero instala Flask (solo la primera vez):
    python -m pip install -r requirements.txt

Despues corres:
    python app.py

Y abres el navegador en http://localhost:5000

La interfaz web tiene un dashboard con las estadisticas, una tabla con todos los
productos, un buscador que filtra mientras escribes, y botones para agregar, editar
y eliminar. Use un tema oscuro con colores azul y morado.


Conceptos de Python que aplique
--------------------------------

Use bastantes cosas del modulo:

- Listas y diccionarios para guardar los productos
- Tuplas para las categorias (porque no cambian)
- Sets para evitar nombres duplicados
- Funciones con parametros y return
- Validaciones con if/elif/else
- Manejo de errores con try/except
- Bucles while para el menu y for para recorrer listas
- break y continue para controlar los loops
- Funciones recursivas (hice factorial y fibonacci como ejemplos)
- Modularizacion: separe todo en archivos diferentes

La estructura de datos principal es una lista global que guarda diccionarios.
Cada producto es un diccionario con: id, nombre, precio, cantidad, categoria
y valor_total (que es precio * cantidad).


Como funciona la version web
-----------------------------

Para la web use Flask. Basicamente cree una API REST que tiene estos endpoints:

GET /api/productos - devuelve todos los productos
POST /api/productos - crea uno nuevo
GET /api/productos/<id> - devuelve uno especifico
PUT /api/productos/<id> - modifica uno existente
DELETE /api/productos/<id> - elimina uno
GET /api/estadisticas - devuelve las stats
GET /api/categorias - devuelve las categorias disponibles

El frontend esta hecho con HTML, CSS y JavaScript puro (sin librerias). Cuando
haces algo en la web (agregar, editar, etc), JavaScript hace un fetch al endpoint
correspondiente y Flask lo procesa usando las mismas funciones de validacion que
la version terminal.

Entonces reutilice todo el codigo del modulo 3, solo le agregue la capa web encima.


Validaciones
------------

Las validaciones estan en validaciones.py y se fijan que:
- Los nombres tengan al menos 3 caracteres
- Los precios sean numeros positivos
- Las cantidades sean enteros positivos
- Las categorias existan en la lista

Si algo esta mal, te avisa y te deja intentar de nuevo.


Cosas que me costaron
---------------------

Al principio tuve problemas con las validaciones porque cuando habia un error se
rompia todo el programa. Despues aprendi a usar try/except y ahi anduvo bien.

Los sets me confundieron un poco al principio, pero cuando entendi que son como
listas pero sin elementos repetidos, los use para evitar productos con nombres
duplicados.

Para la version web tuve que aprender Flask, pero no fue tan complicado. Lo mas
dificil fue entender como conectar el frontend con el backend.


Posibles mejoras
----------------

Si tuviera mas tiempo le agregaria:
- Guardar los productos en un archivo o base de datos (ahora cuando cierras el
  programa se pierden todos)
- Sistema de login para diferentes usuarios
- Poder exportar los datos a Excel o PDF
- Graficos para visualizar las estadisticas
- Subir fotos de los productos


Requisitos
----------

Necesitas Python 3.7 o superior.

Para la version terminal no necesitas nada mas.

Para la version web necesitas:
- Flask 3.0 o superior
- Flask-CORS 4.0 o superior

Los instalas con: python -m pip install -r requirements.txt


Notas
-----

Este proyecto me sirvio mucho para practicar lo que vimos en el modulo. Lo que
mas me gusto fue aprender a organizar el codigo en modulos separados, hace que
sea mucho mas facil de entender y mantener.

La version web la hice como extra, pero la terminal cumple con todo lo que pedia
el modulo.
