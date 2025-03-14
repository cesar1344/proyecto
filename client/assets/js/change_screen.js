document.getElementById('login').addEventListener('click',function() {window.location.href='./index_login.html';});
document.getElementById('nuevo_usuario').addEventListener('click',function() {window.location.href='./index_register.html';});
document.getElementById('nueva_prenda').addEventListener('click',function() {window.location.href='./index_create_clothes.html';});

//cargar pie de pagina //

document.addEventListener("DOMContentLoaded", () => {
    // Selecciona el template
    const template = document.getElementById("pie_de_pagina");
    
    if (template) {
        // Clona el contenido del template
        const clone = template.content.cloneNode(true);

        // Inserta el contenido clonado en el cuerpo del documento (antes del footer)
        document.body.insertBefore(clone, document.querySelector("footer"));
    }
});

//cargar pantalla_compra y cambio de informacion ///


function mostrarProducto(nombre, precio, color, descripcion, imagen) {
    // Agregar la nueva pantalla al historial del navegador
    history.pushState({ page: "producto" }, "", "#producto");

    let pieDePagina = document.getElementById("lastColection");
    if (pieDePagina) {
        pieDePagina.style.display = "none";
    }

    let footer = document.querySelector("footer");
    if (footer) {
        footer.style.display = "block";
    }

    const templateCompra = document.getElementById("pantalla_compra");
    const clonCompra = templateCompra.content.cloneNode(true);

    clonCompra.querySelector("#imgproducto").src = imagen;
    clonCompra.querySelector("#title").textContent = nombre;
    clonCompra.querySelector("#price").textContent = precio;
    clonCompra.querySelector("#color").textContent = "Color: " + color;
    clonCompra.querySelector("#information").innerHTML = descripcion;

    document.body.insertBefore(clonCompra, footer);

    document.getElementById("containerproducto").style.display = "block";
    document.getElementById("buysimformation").style.display = "block";
}

// Manejar el botón de retroceso del navegador
window.addEventListener("popstate", function (event) {
    if (!event.state || event.state.page !== "producto") {
        location.reload(); // Recargar la página principal
    } else {
        // Opcional: Puedes hacer que se vuelva a mostrar el listado de productos sin recargar
        document.getElementById("containerproducto").style.display = "none";
        document.getElementById("buysimformation").style.display = "none";
        document.getElementById("lastColection").style.display = "block";
    }
});

//cargar carrito de compras//




