//Funcion clima
(function () {
    'use strict';
  
    function obtenerClima() {
      fetch('https://api.openweathermap.org/data/2.5/weather?lat=-33.0393&lon=-71.6273&appid=48880986d11f75712c519ce1dee1afd0&lang=es')
        .then(response => response.json())
        .then(data => {
          if (data.main) {
            const weatherDiv = document.getElementById('clima');
            const temperature = data.main.temp - 273.15;
            const description = data.weather[0].description;
            const weatherIcon = document.getElementById('icono-clima');
            const iconCode = data.weather[0].icon;
            const iconUrl = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;
  
            weatherDiv.innerHTML = `<p>La temperatura en Valparaíso es ${temperature.toFixed(1)}°C con ${description}.</p>`;
            weatherIcon.src = iconUrl;
            weatherIcon.alt = description;
            weatherIcon.style.display = 'block';
          } else {
            console.error('Datos inválidos de clima:', data);
          }
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }
  
    document.addEventListener('DOMContentLoaded', obtenerClima);
  })();
  
  //Funcion hora
  
  document.addEventListener('DOMContentLoaded', function () {
    'use strict';
  
    function obtenerHora() {
        const timezone = { id: 'hora-santiago', timezone: 'America/Santiago' };
  
        const url = `https://worldtimeapi.org/api/timezone/${timezone.timezone}`;
  
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(`Datos para ${timezone.timezone}:`, data);  // Verificar datos en la consola
  
                if (data && data.datetime) {
                    const horaDiv = document.getElementById(timezone.id);
                    const hora = new Date(data.datetime);
                    const formattedTime = hora.toLocaleTimeString('es-CL', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
                    const formattedDate = hora.toLocaleDateString('es-CL', { year: 'numeric', month: 'long', day: 'numeric' });
                    horaDiv.innerHTML = `<p>${formattedDate}</p><p>${formattedTime}</p>`;
                } else {
                    console.error('Datos inválidos de hora:', data);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
  
    obtenerHora();
    setInterval(obtenerHora, 1000); // Actualizar cada 5 segundos
  });