document.addEventListener("DOMContentLoaded", function() {

    // Funciones error y confirmación
    function errorAlert(contenedor, mensaje) {
        contenedor.classList.remove("alert", "alert-success");
        contenedor.classList.add("alert", "alert-danger");
        contenedor.innerHTML=mensaje;
        contenedor.style.display="block";
    }

    function successAlert(contenedor, mensaje) {
        contenedor.classList.remove("alert", "alert-danger");
        contenedor.classList.add("alert", "alert-success");
        contenedor.innerHTML=mensaje;
        contenedor.style.display="block";
        setTimeout(function() {
            contenedor.style.display= "none";
            contenedor.innerHTML="";
        }, 2000)
    }

    // Validación Email
    const emailInput = document.getElementById("id_email");
    const emailValidation = document.getElementById("email-validation");
    // Mostrar mensajes de error
    //Selección de campo
    emailInput.addEventListener("focus", function(e) {
        const email = emailInput.value;
        const emailValid = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(email); //Validación de email
        usernameValidation.style.display = "none";
        passwordValidation.style.display = "none";
        confirmValidation.style.display = "none";
        if (!emailValid) {
            errorAlert(emailValidation, "Ingresa un correo electrónico válido.");
            emailInput.setCustomValidity("El correo electrónico es inválido.");
            emailInput.focus();
            e.preventDefault();
        } else {
            emailValidation.style.display="";
            emailValidation.style.display= "none";
        }
    });

    //Desenfoque del campo
    emailInput.addEventListener("blur", function() {
        const email = emailInput.value;
        const emailValid = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(email);
        if (!emailValid) {
            errorAlert(emailValidation, "Ingresa un correo electrónico válido.");
        } else {
            emailInput.setCustomValidity("");
            emailValidation.innerHTML="";
            emailValidation.style.display="none";
        } 
    });

    //Corrección en tiempo real}
    emailInput.addEventListener("input", function() {
        const email = emailInput.value;
        const emailValid = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(email);
        if (!emailValid) {
            errorAlert(emailValidation, "Ingresa un correo electrónico válido.");
        } else {
            successAlert(emailValidation, "Email válido!");
        }
    })
    // Validación Nombre de usuario
    const usernameInput = document.getElementById("id_username");
    const usernameValidation = document.getElementById("username-validation");

    usernameInput.addEventListener("focus", function(e) {
        const username = usernameInput.value;
        const charValid = /^[a-zA-Z0-9]+$/;
        emailValidation.style.display = "none";
        passwordValidation.style.display = "none";
        confirmValidation.style.display = "none";
        if (!charValid.test(username)) {
            errorAlert(usernameValidation, "Máximo 16 caracteres. <br> Solo se permiten las letras y los números.");
            usernameInput.setCustomValidity("El nombre de usuario es inválido.");
            usernameInput.focus();
            e.preventDefault();
        } else {
            usernameValidation.innerHTML=""
            usernameValidation.style.display="none"
        }
    });

    usernameInput.addEventListener("blur", function() {
        const username = usernameInput.value;
        const charValid = /^[a-zA-Z0-9]+$/; // Solo se permiten mayúsculas, minúsculas y números
        if (!charValid.test(username)) {
            errorAlert(usernameValidation, "Usa solamente caracteres válidos (letras o números).");
        } else {
            usernameInput.setCustomValidity("");
            usernameValidation.innerHTML="";
            usernameValidation.style.display= "none";
        }
    });
    usernameInput.addEventListener("input", function() {
        const username = usernameInput.value;
        const charValid = /^[a-zA-Z0-9]+$/;
        if (!charValid.test(username)) {
            errorAlert(usernameValidation, "Usa solamente caracteres válidos (letras o números).");
        } else {
            successAlert(usernameValidation, "Usuario válido!");
        }
    });
    // Validación Contraseña
    const passwordInput = document.getElementById("id_password1"); //Extracción de "password1" del html
    const confirmPasswordInput = document.getElementById("id_password2");
    const passwordValidation = document.getElementById("password-validation"); //Espacio donde se mostrarán los errores de validación (<div>)
    const confirmValidation = document.getElementById("confirm-validation");

    // Mostrar/ocultar mensajes de validación
    passwordInput.addEventListener("focus", function(e) {  //Mostrar
        const contraseña = passwordInput.value;
        const checkContraseña = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,16}$/.test(contraseña);
        usernameValidation.style.display = "none";
        emailValidation.style.display = "none";
        confirmValidation.style.display = "none";
        if (!checkContraseña) {
            errorAlert(passwordValidation, "Tu contraseña debe tener 8 caracteres como mínimo (y 16 como máximo). <br> Tu contraseña debe contener, al menos, una minúscula, un número y una mayúscula.");
            passwordInput.setCustomValidity("La contraseña es inválida.");
            passwordInput.focus();
            e.preventDefault(); //evita acumulación de mensajes
        } else {
            passwordValidation.innerHTML = "";
            passwordValidation.style.display = "none";
        }
    });
    
    passwordInput.addEventListener("blur", function() {  //Ocultar
        const contraseña = passwordInput.value;
        if (contraseña.length < 8) {
            errorAlert(passwordValidation, "La contraseña actual es inválida.");
        } else if (!/[a-z]/.test(contraseña) || !/[A-Z]/.test(contraseña) || !/[0-9]/.test(contraseña)) {
            errorAlert(passwordValidation, "La contraseña actual es inválida");
        } else {
            passwordInput.setCustomValidity("");
            passwordValidation.innerHTML=""; // La contraseña cumple las validaciones
            passwordValidation.style.display = "none";
        }
    });
    passwordInput.addEventListener("input", function() { //Control del campo de contraseña en tiempo real
        const contraseña = passwordInput.value;
        if (contraseña.length < 8) {
            errorAlert(passwordValidation, "La contraseña debe tener 8 caracteres como mínimo.");
        } else if (!/[a-z]/.test(contraseña)) {
            errorAlert(passwordValidation, "La contraseña debe incluir una minúscula.");
        } else if (!/[A-Z]/.test(contraseña)) {
            errorAlert(passwordValidation, "La contraseña debe incluir una mayúscula.");
        } else if (!/[0-9]/.test(contraseña)) {
            errorAlert(passwordValidation, "La contraseña debe incluir un número.");
        } else {
            successAlert(passwordValidation, "Contraseña válida!");
        }
    });

    confirmPasswordInput.addEventListener("focus", function(e) {
        const contraseña1 = passwordInput.value;
        const contraseña2 = confirmPasswordInput.value;
        usernameValidation.style.display = "none";
        passwordValidation.style.display = "none";
        emailValidation.style.display = "none";
        
        if (contraseña1 != contraseña2) {
            errorAlert(confirmValidation, "Tus contraseñas no coinciden.");
            confirmPasswordInput.setCustomValidity("Tus contraseñas no coinciden.");
            confirmPasswordInput.focus();
            e.preventDefault();
        } else {
            confirmValidation.innerHTML=""
            confirmValidation.style.display= "none"
        }
   });

    confirmPasswordInput.addEventListener("blur", function() {
        const contraseña1 = passwordInput.value;
        const contraseña2 = confirmPasswordInput.value;
        if (contraseña1 != contraseña2) {
            errorAlert(confirmValidation, "Tus contraseñas no coinciden.");
        } else {
            confirmPasswordInput.setCustomValidity("");
            confirmValidation.innerHTML=""
            confirmValidation.style.display= "none"
        }
   });

    confirmPasswordInput.addEventListener("input", function() {
        const contraseña1 = passwordInput.value;
        const contraseña2 = confirmPasswordInput.value;
        if (contraseña1 != contraseña2) {
            errorAlert(confirmValidation, "Tus contraseñas no coinciden.");
        } else {
            successAlert(confirmValidation, "Contraseña confirmada!");
        }
    });
});

