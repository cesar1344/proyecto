document.getElementById('login').addEventListener('click',function() {window.location.href='./index_login.html';});
document.getElementById('nuevo_usuario').addEventListener('click',function() {window.location.href='./index_register.html';});
document.getElementById('nueva_prenda').addEventListener('click',function() {window.location.href='./index_create_clothes.html';});


function cargarProducto() {
    console.log("Cargando producto...");

    // Obtener datos del localStorage (estos se guardan en la pantalla anterior)
    const nombre = localStorage.getItem("producto_nombre");
    const precio = localStorage.getItem("producto_precio");
    const color = localStorage.getItem("producto_color");
    const descripcion = localStorage.getItem("producto_descripcion");
    const imagen = localStorage.getItem("producto_imagen");

    console.log("Datos obtenidos:", { nombre, precio, color, descripcion, imagen });

    // Validar si los datos existen antes de mostrarlos
    if (nombre && precio && descripcion && imagen) {
        document.getElementById("title").innerText = nombre;
        document.getElementById("price").innerText = `$ ${precio}`;
        document.getElementById("color").innerHTML = `Color: <span>${color}</span>`;
        document.getElementById("information").innerText = descripcion;
        document.getElementById("imgproducto").src = imagen;
        document.getElementById("imgproducto").alt = nombre;
    } else {
        // Si no hay datos en localStorage, mostrar un mensaje
        document.getElementById("title").innerText = "Producto no encontrado";
        document.getElementById("information").innerText = "No hay detalles disponibles.";
    }
}

// Llamar a la función cuando cargue la página
window.onload = cargarProducto;

