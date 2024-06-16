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

