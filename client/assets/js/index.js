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

// Usamos DOMContentLoaded para asegurarnos de que el DOM está cargado
document.addEventListener("DOMContentLoaded", function() {
    // Función para agregar los productos al contenedor
    function cargarCamisetas() {
        // Obtener el contenedor con el ID "lastCollection"
        const contenedor = document.getElementById("lastColection");

        if (!contenedor) {
            console.error("El contenedor con id 'lastCollection' no se encontró.");
            return;  // Si el contenedor no existe, salir de la función
        }

        // Recorrer el array de productos
        lastCollectionCamisetas.forEach(camiseta => {
            // Crear un contenedor para cada camiseta
            const camisetaDiv = document.createElement("div");
            camisetaDiv.classList.add("camiseta");

            // Crear un elemento de imagen
            const imagen = document.createElement("img");
            imagen.src = camiseta.imagen;
            imagen.alt = camiseta.nombreProducto;

            // Crear un contenedor de información
            const infoDiv = document.createElement("div");
            infoDiv.classList.add("info");

            // Crear nombre y precio de la camiseta
            const nombre = document.createElement("h3");
            nombre.textContent = camiseta.nombreProducto;

            const precio = document.createElement("p");
            precio.textContent = `$${camiseta.precio.toFixed(2)}`;

            // Agregar todo al contenedor de la camiseta
            infoDiv.appendChild(nombre);
            infoDiv.appendChild(precio);
            camisetaDiv.appendChild(imagen);
            camisetaDiv.appendChild(infoDiv);

            // Agregar la camiseta al contenedor principal
            contenedor.appendChild(camisetaDiv);
        });
    }

    // Llamar a la función para cargar las camisetas
    cargarCamisetas();
});
