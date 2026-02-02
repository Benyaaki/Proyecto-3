const API_URL = 'http://localhost:5000/api';

let productos = [];
let categorias = [];
let productoEditando = null;
let productoEliminar = null;

document.addEventListener('DOMContentLoaded', () => {
    cargarCategorias();
    cargarProductos();
    configurarBusqueda();
});

async function cargarProductos() {
    try {
        const response = await fetch(`${API_URL}/productos`);
        const data = await response.json();

        if (data.success) {
            productos = data.productos;
            renderizarProductos(productos);
            actualizarEstadisticas();
        } else {
            mostrarToast('Error al cargar productos', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        mostrarToast('Error de conexión con el servidor', 'error');
    }
}

async function cargarCategorias() {
    try {
        const response = await fetch(`${API_URL}/categorias`);
        const data = await response.json();

        if (data.success) {
            categorias = data.categorias;
            renderizarCategorias();
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function cargarEstadisticas() {
    try {
        const response = await fetch(`${API_URL}/estadisticas`);
        const data = await response.json();

        if (data.success) {
            return data.estadisticas;
        }
    } catch (error) {
        console.error('Error:', error);
    }
    return null;
}

function renderizarProductos(productosAMostrar) {
    const tbody = document.getElementById('products-tbody');
    const emptyState = document.getElementById('empty-state');
    const table = document.getElementById('products-table');

    if (productosAMostrar.length === 0) {
        table.style.display = 'none';
        emptyState.style.display = 'block';
        return;
    }

    table.style.display = 'table';
    emptyState.style.display = 'none';

    tbody.innerHTML = productosAMostrar.map(producto => `
        <tr>
            <td>${String(producto.id).padStart(3, '0')}</td>
            <td><strong>${producto.nombre}</strong></td>
            <td>$${producto.precio.toFixed(2)}</td>
            <td>${producto.cantidad}</td>
            <td><span class="badge">${producto.categoria}</span></td>
            <td><strong>$${producto.valor_total.toFixed(2)}</strong></td>
            <td>
                <button class="btn btn-sm btn-secondary" onclick="editarProducto(${producto.id})" title="Editar">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"></path>
                        <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                    </svg>
                </button>
                <button class="btn btn-sm btn-danger" onclick="abrirModalEliminar(${producto.id})" title="Eliminar">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polyline points="3 6 5 6 21 6"></polyline>
                        <path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"></path>
                    </svg>
                </button>
            </td>
        </tr>
    `).join('');
}

function renderizarCategorias() {
    const select = document.getElementById('categoria');
    select.innerHTML = '<option value="">Seleccione una categoría</option>' +
        categorias.map(cat => `<option value="${cat}">${cat}</option>`).join('');
}

async function actualizarEstadisticas() {
    const stats = await cargarEstadisticas();

    if (stats) {
        document.getElementById('stat-total').textContent = stats.total_productos;
        document.getElementById('stat-unidades').textContent = stats.total_unidades.toLocaleString();
        document.getElementById('stat-valor').textContent = `$${stats.valor_total.toLocaleString('es-ES', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
        document.getElementById('stat-promedio').textContent = `$${stats.precio_promedio.toLocaleString('es-ES', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
    }
}

function configurarBusqueda() {
    const searchInput = document.getElementById('search-input');

    searchInput.addEventListener('input', (e) => {
        const termino = e.target.value.toLowerCase();

        if (termino === '') {
            renderizarProductos(productos);
        } else {
            const productosFiltrados = productos.filter(p =>
                p.nombre.toLowerCase().includes(termino) ||
                p.categoria.toLowerCase().includes(termino) ||
                String(p.id).includes(termino)
            );
            renderizarProductos(productosFiltrados);
        }
    });
}

function abrirModal() {
    productoEditando = null;
    document.getElementById('modal-title').innerHTML = `
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
        </svg>
        Agregar Producto
    `;
    document.getElementById('submit-btn').textContent = 'Guardar';
    document.getElementById('product-form').reset();
    document.getElementById('product-modal').classList.add('active');
}

function cerrarModal() {
    document.getElementById('product-modal').classList.remove('active');
    productoEditando = null;
}

function abrirModalEliminar(id) {
    const producto = productos.find(p => p.id === id);
    if (producto) {
        productoEliminar = id;
        document.getElementById('delete-product-name').textContent = producto.nombre;
        document.getElementById('delete-modal').classList.add('active');
    }
}

function cerrarModalEliminar() {
    document.getElementById('delete-modal').classList.remove('active');
    productoEliminar = null;
}

window.addEventListener('click', (e) => {
    const productModal = document.getElementById('product-modal');
    const deleteModal = document.getElementById('delete-modal');

    if (e.target === productModal) {
        cerrarModal();
    }
    if (e.target === deleteModal) {
        cerrarModalEliminar();
    }
});

async function guardarProducto(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const producto = {
        nombre: formData.get('nombre'),
        precio: parseFloat(formData.get('precio')),
        cantidad: parseInt(formData.get('cantidad')),
        categoria: formData.get('categoria')
    };

    try {
        let response;

        if (productoEditando) {

            response = await fetch(`${API_URL}/productos/${productoEditando}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(producto)
            });
        } else {

            response = await fetch(`${API_URL}/productos`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(producto)
            });
        }

        const data = await response.json();

        if (data.success) {
            mostrarToast(data.message, 'success');
            cerrarModal();
            cargarProductos();
        } else {
            mostrarToast(data.error, 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        mostrarToast('Error al guardar el producto', 'error');
    }
}

async function editarProducto(id) {
    const producto = productos.find(p => p.id === id);

    if (producto) {
        productoEditando = id;
        document.getElementById('modal-title').innerHTML = `
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"></path>
                <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"></path>
            </svg>
            Editar Producto
        `;
        document.getElementById('submit-btn').textContent = 'Actualizar';

        document.getElementById('nombre').value = producto.nombre;
        document.getElementById('precio').value = producto.precio;
        document.getElementById('cantidad').value = producto.cantidad;
        document.getElementById('categoria').value = producto.categoria;

        document.getElementById('product-modal').classList.add('active');
    }
}

async function confirmarEliminar() {
    if (!productoEliminar) return;

    try {
        const response = await fetch(`${API_URL}/productos/${productoEliminar}`, {
            method: 'DELETE'
        });

        const data = await response.json();

        if (data.success) {
            mostrarToast(data.message, 'success');
            cerrarModalEliminar();
            cargarProductos();
        } else {
            mostrarToast(data.error, 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        mostrarToast('Error al eliminar el producto', 'error');
    }
}

function mostrarToast(mensaje, tipo = 'info') {
    const container = document.getElementById('toast-container');

    const toast = document.createElement('div');
    toast.className = `toast ${tipo}`;

    let iconSvg = '';
    if (tipo === 'success') {
        iconSvg = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>`;
    } else if (tipo === 'error') {
        iconSvg = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="15" y1="9" x2="9" y2="15"></line>
            <line x1="9" y1="9" x2="15" y2="15"></line>
        </svg>`;
    } else {
        iconSvg = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="16" x2="12" y2="12"></line>
            <line x1="12" y1="8" x2="12.01" y2="8"></line>
        </svg>`;
    }

    toast.innerHTML = `
        <div style="color: var(--primary-light);">${iconSvg}</div>
        <span>${mensaje}</span>
    `;

    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => {
            container.removeChild(toast);
        }, 300);
    }, 3000);
}

function formatearMoneda(valor) {
    return new Intl.NumberFormat('es-ES', {
        style: 'currency',
        currency: 'USD'
    }).format(valor);
}

function formatearNumero(valor) {
    return new Intl.NumberFormat('es-ES').format(valor);
}
