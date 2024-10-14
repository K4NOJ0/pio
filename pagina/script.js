document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('reviewForm');
    const commentSection = document.getElementById('commentSection');

    // Cargar comentarios al inicio
    cargarComentarios();

    // Escuchar el envío del formulario
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const nombre = document.getElementById('nombre').value;
        const comentario = document.getElementById('comentario').value;
        const rating = document.getElementById('rating').value;

        // Crear el objeto del comentario
        const nuevoComentario = {
            nombre: nombre,
            comentario: comentario,
            rating: rating
        };

        // Guardar el comentario en el LocalStorage
        guardarComentario(nuevoComentario);

        // Agregar el nuevo comentario a la página
        agregarComentario(nuevoComentario);

        // Limpiar el formulario
        form.reset();
    });

    // Función para cargar los comentarios desde LocalStorage
    function cargarComentarios() {
        const comentarios = JSON.parse(localStorage.getItem('comentarios')) || [];
        comentarios.forEach(comentario => agregarComentario(comentario));
    }

    // Función para guardar el comentario en LocalStorage
    function guardarComentario(comentario) {
        const comentarios = JSON.parse(localStorage.getItem('comentarios')) || [];
        comentarios.push(comentario);
        localStorage.setItem('comentarios', JSON.stringify(comentarios));
    }

    // Función para agregar un comentario al DOM
    function agregarComentario(comentario) {
        const review = document.createElement('article');
        review.classList.add('review');
        
        review.innerHTML = `
            <h3>Usuario: ${comentario.nombre}</h3>
            <p>${comentario.comentario}</p>
            <div class='rating'>Calificación: ${comentario.rating}</div>
        `;
        commentSection.appendChild(review);
    }
});