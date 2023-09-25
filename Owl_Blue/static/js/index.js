// Mensaje de bienvenida
document.addEventListener('DOMContentLoaded', function () {
    // Obtiene el mensaje de confirmación
    var mensajeConfirmacion = document.getElementById('check');
    // Verifica si el mensaje de confirmación existe
    if (mensajeConfirmacion) {
        mensajeConfirmacion.style.display = 'block';
        setTimeout(function () {
            mensajeConfirmacion.style.display = 'none';
        }, 3000); // Oculta el mensaje (3 sec después)
    }
});
