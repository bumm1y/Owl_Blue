// Mensaje de bienvenida
document.addEventListener('DOMContentLoaded', function () { // Verificador de la carga del html
    
    // Función mensaje de confirmaci{on}
    function successAlert(contenedor, mensaje) {
        //manejo de clases html
        contenedor.classList.add("alert", "alert-success"); 
        contenedor.innerHTML=mensaje;
        contenedor.style.display="block";
        setTimeout(function() {
            contenedor.classList.remove("alert", "alert-success");
            contenedor.style.display= "none";
            contenedor.innerHTML="";
        }, 2000)
    }
    var mensajeConfirmacion = document.getElementById('bienvenida');
    // Verifica si el mensaje de confirmación existe
    if (mensajeConfirmacion) {
        successAlert(mensajeConfirmacion, mensajeConfirmacion.innerHTML);
    }
});
