function mostrarProducto(nombre, precio, color, descripcion, imagen) {
    console.log("Guardando datos en localStorage...");

    // Guardar en localStorage
    localStorage.setItem("producto_nombre", nombre);
    localStorage.setItem("producto_precio", precio);
    localStorage.setItem("producto_color", color);
    localStorage.setItem("producto_descripcion", descripcion);
    localStorage.setItem("producto_imagen", imagen);

    console.log("Datos guardados:", { nombre, precio, color, descripcion, imagen });

    // Redireccionar a la página de compra
    window.location.href = "index_compra.html";
}

// Función para cargar los datos en la página de compra
function cargarProducto() {
    console.log("Ejecutando cargarProducto()...");

    // Obtener los datos guardados
    const nombre = localStorage.getItem("producto_nombre");
    const precio = localStorage.getItem("producto_precio");
    const color = localStorage.getItem("producto_color");
    const descripcion = localStorage.getItem("producto_descripcion");
    const imagen = localStorage.getItem("producto_imagen");

    console.log("Datos cargados:", { nombre, precio, color, descripcion, imagen });

    // Validar si hay datos
    if (nombre && precio && descripcion && imagen) {
        document.getElementById("titulo").innerText = nombre;
        document.getElementById("descripcion").innerText = `${descripcion} - Color: ${color}`;
        document.getElementById("precio").innerText = `Precio: ${precio}`;
        document.getElementById("img").src = imagen;
        document.getElementById("img").alt = nombre;
    } else {
        document.getElementById("detalle_titulo").innerText = "No se encontraron datos del producto.";
    }
}
