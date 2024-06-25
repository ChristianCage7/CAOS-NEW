(function () {



    //Header y footer constantes
    const footer = document.querySelector("footer");
    
    // Header Dinámico
    function createNavbar() {
      const navbarHTML = `
      <nav class="navbar navbar-expand-lg bg-body-tertiary fixed-top">
          <div class="container-fluid">
              <a class="navbar-brand" href="templates/index.html">
                  <img src="{% static 'img/logopeque.png' %}" alt="Logo" width="140" height="80" class="d-inline-block align-text-top">
              </a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                  data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                  aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                      <li class="nav-item dropdown">
                          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                              aria-expanded="false">Categorias</a>
                          <ul class="dropdown-menu">
                              <li><a class="dropdown-item" href="/categorias/cat_politica.html">Política</a></li>
                              <li><a class="dropdown-item" href="/categorias/cat_deportes.html">Deporte</a></li>
                              <li><a class="dropdown-item" href="/categorias/cat_internacional.html">Internacional</a></li>
                              <li><a class="dropdown-item" href="/categorias/cat_economia.html">Economía</a></li>
                          </ul>
                      </li>
                      <li class="nav-item">
                          <a class="nav-link" href="/quienes_somos.html">¿Quiénes somos?</a>
                      </li>
                  </ul>
                  <ul class="navbar-nav">
                      <li class="nav-item dropdown">
                          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                              aria-expanded="false">Usuario</a>
                          <ul class="dropdown-menu">
                              <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                      data-bs-target="#loginModal">Iniciar Sesión</a></li>
                              <li><a class="dropdown-item" href="#" data-bs-toggle="modal"
                                      data-bs-target="#registerModal">Registrarse</a></li>
                          </ul>
                      </li>
                      <li class="nav-item">
                          <a class="btn btn-warning" href="/planes.html">Suscríbete aquí</a>
                      </li>
                  </ul>
                  <form class="d-flex" role="search">
                      <input class="form-control me-2" type="search" placeholder="¿Qué necesitas?" aria-label="Search">
                      <button class="btn btn-outline-danger" type="submit">Buscar</button>
                  </form>
              </div>
          </div>
      </nav>
      `;
      document.body.insertAdjacentHTML('afterbegin', navbarHTML);
    }
    
    function createModals() {
      const modalsHTML = `
      <!-- Modal para iniciar sesión -->
      <div class="modal fade" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
          <div class="modal-dialog">
              <div class="modal-content">
                  <div class="modal-header">
                      <img src="{% static 'img/logopeque.png' %}" alt="pequeño logo" width="50"> Iniciar Sesión
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                      <form class="needs-validation" novalidate>
                          <div class="form-group">
                              <label for="exampleInputEmail1">Correo electrónico</label>
                              <input type="email" class="form-control" id="exampleInputEmail1"
                                  aria-describedby="emailHelp" placeholder="Ingresar email" required>
                              <div class="invalid-feedback">
                                  Por favor ingrese un correo válido
                              </div>
                          </div>
                          <br>
                          <div class="form-group">
                              <label for="exampleInputPassword1">Contraseña</label>
                              <input type="password" class="form-control" id="exampleInputPassword1"
                                  placeholder="Ingresar contraseña" required>
                              <div class="invalid-feedback">
                                  Por favor ingrese su contraseña
                              </div>
                          </div>
                          <br>
                          <button type="submit" class="btn btn-primary">Ingresar</button>
                      </form>
                  </div>
              </div>
          </div>
      </div>
      <!-- Modal para registrarse -->
      <div class="modal fade" id="registerModal" tabindex="-1" aria-labelledby="registerModalLabel" aria-hidden="true">
          <div class="modal-dialog">
              <div class="modal-content">
                  <div class="modal-header">
                      <img src="{% static 'img/logopeque.png' %}" alt="pequeño logo" width="50">Registrarse
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                      <form class="needs-validation" novalidate>
                          <div class="form-group">
                              <label for="exampleInputName">Nombre</label>
                              <input type="text" class="form-control" id="exampleInputName"
                                  aria-describedby="nameHelp" placeholder="Ingresar nombre" required>
                              <div class="invalid-feedback">
                                  Por favor ingrese su nombre
                              </div>
                          </div>
                          <br>
                          <div class="form-group">
                              <label for="exampleInputLastName">Apellido</label>
                              <input type="text" class="form-control" id="exampleInputLastName"
                                  aria-describedby="lastNameHelp" placeholder="Ingresar apellido" required>
                              <div class="invalid-feedback">
                                  Por favor ingrese su apellido
                              </div>
                          </div>
                          <br>
                          <div class="form-group">
                              <label for="exampleInputEmail1">Correo electrónico</label>
                              <input type="email" class="form-control" id="exampleInputEmail1"
                                  aria-describedby="emailHelp" placeholder="Ingresar email" required>
                              <div class="invalid-feedback">
                                  Por favor ingrese un correo válido
                              </div>
                              <small id="emailHelp" class="form-text text-muted">Su correo electrónico no será compartido</small>
                          </div>
                          <br>
                          <div class="form-group">
                              <label for="exampleInputPassword1">Contraseña</label>
                              <input type="password" class="form-control" id="exampleInputPassword1"
                                  placeholder="Ingresar contraseña" required>
                              <div class="invalid-feedback">
                                  Por favor ingrese su contraseña
                              </div>
                          </div>
                          <br>
                          <button type="submit" class="btn btn-primary">Registrarse</button>
                      </form>
                  </div>
              </div>
          </div>
      </div>
      `;
      document.body.insertAdjacentHTML('beforeend', modalsHTML);
    }
    
    document.addEventListener("DOMContentLoaded", function() {
      createNavbar();
      createModals();
    });
    
    // Footer Dinámico
    document.addEventListener("DOMContentLoaded", function() {
      var footerContainer = document.getElementById('footer-container');
    
      if(footerContainer) {
        var footerHTML = `
          <footer class="footer bg-dark text-center py-3">
            <div class="container">
              <img src="{% static 'img/logoblancotrans.png' %}" alt="Logo" width="250" height="150">
              <br>
              Todos los derechos reservados.
            </div>
          </footer>
        `;
    
        footerContainer.innerHTML = footerHTML;
      }
    });
    
    // JavaScript para cambiar el tamaño y color del navbar al hacer scroll
    document.addEventListener("DOMContentLoaded", function() {
      var navbar = document.querySelector(".navbar");
      var navbarBrand = document.querySelector(".navbar-brand img");
    
    
      // Añadir la clase y ajustar el tamaño del logo al hacer scroll
      window.addEventListener("scroll", adjustNavbar);
    });
    
    })();
    
    