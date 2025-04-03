////cambio de color /// 
function changeShirtColor(color) {
    let tshirtImage = document.getElementById("tshirt");

    // Verifica si el elemento existe antes de cambiar la imagen
    if (tshirtImage) {
        // Mapeo de colores con imágenes
        let colorMap = {
            "red": "./assets/img/camisetas/t-shirt_red.png",
            "blue": "./assets/img/camisetas/t-shirt_blue.png",
            "green": "./assets/img/camisetas/t-shirt_green.png",
            "yellow": "./assets/img/camisetas/t-shirt_yellow.png",
            "black": "./assets/img/camisetas/t-shirt_black.png",
            "orangered": "./assets/img/camisetas/t-shirt_orangered.png",
            "grey": "./assets/img/camisetas/t-shirt_grey.png",
            "white": "./assets/img/camisetas/t-shirt_white.png"
        };

        // Cambia la imagen de la camiseta si el color está en el mapeo
        if (colorMap[color]) {
            tshirtImage.src = colorMap[color];
        } else {
            console.error("No se encontró la imagen para el color:", color);
        }
    } else {
        console.error("No se encontró el elemento con id 'tshirt'");
    }
}
//// texto // 
document.addEventListener("DOMContentLoaded", function () {
    let input = document.getElementById("textInput");
    let buttonText = document.getElementById("textButton");
    let isDragging = false;
    let offsetX = 0, offsetY = 0;

    // Mostrar/Ocultar el input al presionar el botón "Texto"
    buttonText.addEventListener("click", function () {
        if (input.style.display === "none" || input.style.display === "") {
            input.style.display = "block";
            input.focus();
        } else {
            input.style.display = "none";
        }
    });

    // Evento para iniciar el movimiento
    input.addEventListener("mousedown", function (e) {
        isDragging = true;

        // Capturar la posición relativa del mouse respecto al input
        offsetX = e.clientX - input.getBoundingClientRect().left;
        offsetY = e.clientY - input.getBoundingClientRect().top;

        // Evita seleccionar texto mientras se mueve
        e.preventDefault();
    });

    // Evento para mover el input
    document.addEventListener("mousemove", function (e) {
        if (isDragging) {
            let tshirt = document.getElementById("tshirt").getBoundingClientRect();
            let inputRect = input.getBoundingClientRect();

            let newX = e.clientX - offsetX;
            let newY = e.clientY - offsetY;

            // Limitar movimiento dentro de la camiseta
            if (newX >= tshirt.left && newX + inputRect.width <= tshirt.right) {
                input.style.left = (newX - tshirt.left) + "px";
            }
            if (newY >= tshirt.top && newY + inputRect.height <= tshirt.bottom) {
                input.style.top = (newY - tshirt.top) + "px";
            }
        }
    });

    // Evento para detener el movimiento
    document.addEventListener("mouseup", function () {
        isDragging = false;
    });
});

///modal logotipos ///

document.addEventListener("DOMContentLoaded", function () {
    let modal = document.getElementById("modalDisenos");
    let btnDisenos = document.getElementById("btnDisenos");
    let closeBtn = document.querySelector(".close");

    // Ocultar modal al inicio
    modal.style.display = "none";

    // Mostrar/Ocultar modal o eliminar diseño al hacer clic en el botón "Diseños"
    btnDisenos.addEventListener("click", function (event) {
        event.preventDefault(); // Evita el comportamiento por defecto del enlace

        let existingDesign = document.querySelector(".tshirt-design");

        if (existingDesign) {
            existingDesign.remove(); // Si hay un diseño, lo elimina
        } else {
            modal.style.display = "flex"; // Si no hay diseño, muestra el modal
        }
    });

    // Cerrar modal al hacer clic en la "X"
    closeBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    // Cerrar modal al hacer clic fuera del contenido
    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

    // Función para seleccionar un diseño y agregarlo a la camiseta
    document.querySelectorAll(".design-img").forEach(img => {
        img.addEventListener("click", function () {
            let tshirt = document.querySelector(".image-section img");
            let design = document.createElement("img");

            design.src = this.src;
            design.classList.add("tshirt-design");
            design.style.position = "absolute";
            design.style.left = "50%";
            design.style.top = "50%";
            design.style.transform = "translate(-50%, -50%)";
            design.style.width = "150px"; // Tamaño del diseño

            // Eliminar diseños anteriores antes de agregar uno nuevo
            let existingDesign = document.querySelector(".tshirt-design");
            if (existingDesign) {
                existingDesign.remove();
            }

            tshirt.parentNode.appendChild(design);
            modal.style.display = "none"; // Cerrar el modal después de seleccionar
        });
    });
});
