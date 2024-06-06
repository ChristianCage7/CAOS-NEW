$(document).ready(function() { //Funciona igual que DOMContentLoaded, carga el archivo solamente en estructura sin CSS.
  // Seleccionar los elementos del formulario
  const form = $("#contactForm");
  const rutInput = $("#rutInput");
  const nombreInput = $("#nombreInput");
  const edadInput = $("#edadInput");
  const generoSelect = $("#generoSelect");
  const celularInput = $("#celularInput");
  const correoInput = $("#correoInput");
  const mensajeTextArea = $("#mensajeTextArea");
  const charCount = $("#charCount");

  // Restablecer el formulario y las validaciones cuando se oculta el modal
  $("#contactModal").on('hidden.bs.modal', function () {
    form[0].reset(); //Resetea el formulario en caso que se esconda
    $(".is-invalid").removeClass('is-invalid'); //Elimina la clase de validaciones para evitar que se ponga rojo al cerrar
  });

  // Validar el formulario antes de enviarlo
  form.on("submit", function (event) { //Trabajamos con funcion anonima que funciona como un manejador de eventos
    event.preventDefault(); //Previene que el formulario se envie, asi verifica las validaciones
    if (form[0].checkValidity()) { //Se checkean la validaciones avanza si es valido
      console.log("Formulario válido. Enviar...");
      $("#contactModal").modal('hide'); // Cierra el modal
    } else {
      $(".is-invalid").removeClass("is-invalid"); //Remueve la clase que los pone en rojo

      if (!rutInput.val().trim()) {
        rutInput.addClass("is-invalid"); 
      }
      if (!nombreInput.val().trim()) {
        nombreInput.addClass("is-invalid");
      }
      if (!edadInput.val().trim()) {
        edadInput.addClass("is-invalid");
      }
      if (!generoSelect.val()) {
        generoSelect.addClass("is-invalid");
      }
      if (!celularInput.val().trim()) {
        celularInput.addClass("is-invalid");
      }
      if (!correoInput.val().trim()) {
        correoInput.addClass("is-invalid");
      }
      if (!mensajeTextArea.val().trim()) {
        mensajeTextArea.addClass("is-invalid");
      }

      // Detener el envío del formulario
      event.stopPropagation();
    }
  });

  // Validaciones personalizadas para el campo de RUT
  rutInput.on("input", function () {
    const rut = rutInput.val().trim(); //TRIM elimina los espacios en blancos del principio y el final
    if (rut.length < 9 || rut.length > 10) {
      rutInput.addClass("is-invalid");
      $("#rutFeedback").text("El Rut debe tener entre 9 y 10 caracteres.");
    } else {
      rutInput.removeClass("is-invalid");
      $("#rutFeedback").text("");
    }
  });

  // Validaciones personalizadas para el campo de nombre
  nombreInput.on("input", function () {
    const nombre = nombreInput.val().trim();
    if (nombre.length < 3 || nombre.length > 20) {
      nombreInput.addClass("is-invalid");
      $("#nombreFeedback").text("El nombre debe tener entre 3 y 20 caracteres.");
    } else {
      nombreInput.removeClass("is-invalid");
      $("#nombreFeedback").text("");
    }
  });

  // Validaciones personalizadas para el campo de edad
  edadInput.on("input", function () {
    const edad = parseInt(edadInput.val());
    if (isNaN(edad) || edad < 18) {
      edadInput.addClass("is-invalid");
      $("#edadFeedback").text("La edad debe ser mayor a 18");
    } else {
      edadInput.removeClass("is-invalid");
      $("#edadFeedback").text("");
    }
  });

  // Validaciones personalizadas para el campo de género
  generoSelect.on("change", function () {
    if (!generoSelect.val()) {
      generoSelect.addClass("is-invalid");
      $("#generoFeedback").text("Por favor selecciona un género.");
    } else {
      generoSelect.removeClass("is-invalid");
      $("#generoFeedback").text("");
    }
  });

  // Validaciones personalizadas para el campo de celular
  celularInput.on("input", function () {
    const celular = celularInput.val().trim();
    if (celular.length < 9 || celular.length > 12) {
      celularInput.addClass("is-invalid");
      $("#celularFeedback").text("El celular debe tener entre 9 y 12 caracteres.");
    } else {
      celularInput.removeClass("is-invalid");
      $("#celularFeedback").text("");
    }
  });

  // Validaciones personalizadas para el campo de correo electrónico
  correoInput.on("input", function () {
    const correo = correoInput.val().trim();
    if (correo.length === 0 || correo.indexOf("@") === -1 || correo.indexOf(".") === -1) {
      correoInput.addClass("is-invalid");
      $("#correoFeedback").text("Por favor ingresa un correo válido.");
    } else {
      correoInput.removeClass("is-invalid");
      $("#correoFeedback").text("");
    }
  });

  // Validaciones personalizadas para el campo de mensaje
  mensajeTextArea.on("input", function () {
    const mensaje = mensajeTextArea.val().trim();
    if (mensaje.length > 300) {
      mensajeTextArea.addClass("is-invalid");
      $("#mensajeFeedback").text("El mensaje no puede exceder los 300 caracteres.");
    } else {
      mensajeTextArea.removeClass("is-invalid");
      $("#mensajeFeedback").text("");
    }
  });

  // Contador de caracteres para el campo de mensaje
  mensajeTextArea.on("input", function () {
    const messageLength = mensajeTextArea.val().length; //Evalua el largo del mensaje
    const maxLength = parseInt(mensajeTextArea.attr("maxlength")); //Toma el largo maximo puesot en el HTML
    const remainingChars = maxLength - messageLength; //Evalua de forma constante los caracteres
    charCount.text(`Caracteres restantes: ${remainingChars}`); //A través del HTML muestra los caracteres restantes
  });
});
