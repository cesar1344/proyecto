// scripts.js
document.getElementById('login_form').addEventListener('submit', function (event) {
    event.preventDefault();

    let email = document.getElementById('user_name').value;
    let password = document.getElementById('password').value;

    let emailError = document.getElementById('error-email');
    let passwordError = document.getElementById('error-password');

    let valid = true;

    // Reiniciar mensajes de error
    emailError.style.display = 'none';
    passwordError.style.display = 'none';

    // Validar correo electrónico
    if (email === '') {
        emailError.textContent = 'Correo incorrecto';
        emailError.style.display = 'block';
        valid = false;
    }

    // Validar contraseña
    if (password === '') {
        passwordError.textContent = 'Contraseña incorrecta';
        passwordError.style.display = 'block';
        valid = false;
    }

    // Si todo es válido, se puede enviar el formulario
    if (valid) {
        // Aquí puedes manejar el envío del formulario
        alert('Formulario enviado con éxito');
    }
});
