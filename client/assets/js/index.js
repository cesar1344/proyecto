const lastCollectionCamisetas = [
    {
        idProducto: 1,
        nombreProducto: "Camiseta Vintage",
        precio: 19.99,
        imagen: "http://127.0.0.1:5500/client/assets/img/camisetas/t-shirt_02.png",
        category: "Camisetas"
    },
    {
        idProducto: 2,
        nombreProducto: "Camiseta Estampada Femenina",
        precio: 24.99,
        imagen: "http://127.0.0.1:5500/client/assets/img/camisetas/t-shirt_07.png",
        category: "Camisetas"
    },
    {
        idProducto: 3,
        nombreProducto: "Camiseta Estampada Masculina",
        precio: 15.49,
        imagen: "http://127.0.0.1:5500/client/assets/img/camisetas/t-shirt_05.png",
        category: "Camisetas"
    },
    {
        idProducto: 4,
        nombreProducto: "Camiseta Básica Femenina",
        precio: 29.99,
        imagen: "http://127.0.0.1:5500/client/assets/img/camisetas/t-shirt_10.png",
        category: "Camisetas"
    },
    {
        idProducto: 5,
        nombreProducto: "Camiseta Básica Masculina",
        precio: 12.99,
        imagen: "http://127.0.0.1:5500/client/assets/img/camisetas/t-shirt_09.png",
        category: "Camisetas"
    }
];

document.addEventListener("DOMContentLoaded", function() {
    function cargarCamisetas() {
        const contenedor = document.getElementById("lastColection");

        if (!contenedor) {
            console.error("El contenedor con id 'lastColection' no se encontró.");
            return;
        }

        lastCollectionCamisetas.forEach(camiseta => {
            const camisetaDiv = document.createElement("div");
            camisetaDiv.classList.add("camiseta");

            const imagen = document.createElement("img");
            imagen.src = camiseta.imagen;
            imagen.alt = camiseta.nombreProducto;

            const infoDiv = document.createElement("div");
            infoDiv.classList.add("info");

            const nombre = document.createElement("h3");
            nombre.textContent = camiseta.nombreProducto;

            const precio = document.createElement("p");
            precio.textContent = `$${camiseta.precio.toFixed(2)}`;

            infoDiv.appendChild(nombre);
            infoDiv.appendChild(precio);
            camisetaDiv.appendChild(imagen);
            camisetaDiv.appendChild(infoDiv);

            // 🚀 Evento de redirección al hacer clic
            camisetaDiv.addEventListener("click", () => {
                window.location.href = `index.compra.html?id=${camiseta.idProducto}&nombre=${encodeURIComponent(camiseta.nombreProducto)}&precio=${camiseta.precio}&imagen=${encodeURIComponent(camiseta.imagen)}`;


            });

            contenedor.appendChild(camisetaDiv);
        });
    }

    cargarCamisetas();
});
