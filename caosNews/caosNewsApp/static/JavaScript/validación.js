// Función modal login y registro
(function () {
  'use strict';
  window.addEventListener('load', function () {
    var forms = document.getElementsByClassName('needs-validation');
    var validation = Array.prototype.filter.call(forms, function (form) {
      form.addEventListener('submit', function (event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function () {
      $('.alert').alert('close');
  }, 3000);  // Cierra las alertas después de 3000 milisegundos = 3 segundos
});


// Mensaje de alerta
document.addEventListener('DOMContentLoaded', function() {
  // Desvanecer el mensaje después de 3 segundos
  setTimeout(function() {
      let alerts = document.querySelectorAll('.alert');
      alerts.forEach(function(alert) {
          alert.classList.remove('show');
          alert.classList.add('fade');
          setTimeout(function() {
              alert.remove();
          }, 600); // Tiempo para eliminar el elemento después de desvanecerse
      });
  }, 3000); // Tiempo antes de empezar a desvanecerse
});