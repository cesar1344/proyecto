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


document.addEventListener("DOMContentLoaded", function () {
    const botonCarrito = document.getElementById("botonCarrito");
    const mainContainer = document.body; // Puedes cambiarlo a otro contenedor si lo necesitas

    if (botonCarrito) {
        botonCarrito.addEventListener("click", function () {
            // Guardar el estado actual en el historial
            history.pushState({ page: "carrito" }, "", "#carrito");

            // Remover cualquier contenido anterior
            document.querySelectorAll("#pie_de_pagina, #pantalla_compra").forEach(el => el.remove());

            // Obtener el template del carrito
            const carritoTemplate = document.getElementById("carrito_compras");
            if (carritoTemplate) {
                const clone = carritoTemplate.content.cloneNode(true);

                // Insertar el contenido del carrito en la página
                mainContainer.innerHTML = ""; // Borra el contenido anterior
                mainContainer.appendChild(clone);
            } else {
                console.error("El template del carrito no se encontró.");
            }
            
            document.body.insertBefore(clonCompra, footer);
        });
    } else {
        console.error("El botón del carrito no se encontró.");
    }

    // Manejar el evento de retroceso del navegador
    window.addEventListener("popstate", function (event) {
        if (!event.state || event.state.page !== "carrito") {
            // Recargar la página o restaurar la pantalla principal
            location.reload(); 
        }
    });
});

///// cargar terminos y condiciones//////
document.addEventListener("DOMContentLoaded", function () {
    const btnTerminos = document.getElementById("btn-terminos");
    const mainContainer = document.body; // Puedes cambiarlo a otro contenedor si lo necesitas

    if (btnTerminos) {
        btnTerminos.addEventListener("click", function (e) {
            e.preventDefault();

            // Guardar el estado actual en el historial
            history.pushState({ page: "terminos" }, "", "#terminos");

            // Remover cualquier contenido anterior (Pie de página o Pantalla de compra)
            document.querySelectorAll("#pie_de_pagina, #pantalla_compra").forEach(el => el.remove());

            // Obtener el template de Términos y Condiciones
            const terminosTemplate = document.getElementById("terminos_Y_condiciones");
            if (terminosTemplate) {
                const clone = terminosTemplate.content.cloneNode(true);

                // Insertar el contenido en la página
                mainContainer.innerHTML = ""; // Borra el contenido anterior
                mainContainer.appendChild(clone);
            } else {
                console.error("El template de términos y condiciones no se encontró.");
            }
        });
    } else {
        console.error("El botón de términos y condiciones no se encontró.");
    }

    // Manejar el evento de retroceso del navegador
    window.addEventListener("popstate", function (event) {
        if (!event.state || event.state.page !== "terminos") {
            // Recargar la página o restaurar la pantalla principal
            location.reload(); 
        }
    });
});

/////////// cargar politicas de privacidad////
document.addEventListener("DOMContentLoaded", function () {
    const btnPolitica = document.getElementById("btn-politica");
    const mainContainer = document.body; // Contenedor principal

    if (btnPolitica) {
        btnPolitica.addEventListener("click", function (e) {
            e.preventDefault();

            // Guardar el estado actual en el historial
            history.pushState({ page: "politica" }, "", "#politica");

            // Remover cualquier contenido anterior (Pie de página o Pantalla de compra)
            document.querySelectorAll("#pie_de_pagina, #pantalla_compra").forEach(el => el.remove());

            // Obtener el template de Política de Privacidad
            const politicaTemplate = document.getElementById("politica_privacidad");
            if (politicaTemplate) {
                const clone = politicaTemplate.content.cloneNode(true);

                // Insertar el contenido en la página
                mainContainer.innerHTML = ""; // Borra el contenido anterior
                mainContainer.appendChild(clone);
            } else {
                console.error("El template de política de privacidad no se encontró.");
            }
        });
    } else {
        console.error("El botón de política de privacidad no se encontró.");
    }

    // Manejar el evento de retroceso del navegador
    window.addEventListener("popstate", function (event) {
        if (!event.state || event.state.page !== "politica") {
            location.reload(); // Recargar la página o restaurar la pantalla principal
        }
    });
});

