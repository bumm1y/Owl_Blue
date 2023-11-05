
document.addEventListener("DOMContentLoaded", function() {
  console.log("hola");
});
    
/*
  function desordenarAlternativas(pregunta) {
    let alternativas = [
      pregunta.respuesta,
      pregunta.alternativa1,
      pregunta.alternativa2,
      pregunta.alternativa3
    ];
    seleccionar_id("btn1").innerHTML = alternativas[0];
    seleccionar_id("btn2").innerHTML = alternativas[1];
    seleccionar_id("btn3").innerHTML = alternativas[2];
    seleccionar_id("btn4").innerHTML = alternativas[3];
  }

  function oprimir_boton(i) {
    if (alternativas[i] == pregunta.respuesta) {
      boton_seleccionado[i].style.background = "lightgreen";
    } else {
      boton_seleccionado[i].style.background = "pink";
    }
    // Condicional de botón siguiente
    reiniciar();
  }

  function reiniciar() {
    for (const boton of boton_seleccionado) {
      boton.style.background = "white";
    }
  }

  function seleccionar_id(id) {
    return document.getElementById(id);
  }

  function style(id) {
    return seleccionar_id(id).style;
  }


  function obtenerDatosJSON() {
    var categoria = categoria_elegida;
    var ruta = 'acts/' + categoria + '/capsula0/lessons/lessonJSON';
    return fetch(ruta)
      .then(response => {
        if (response.ok) {
          return.json();
        };
  }

  obtenerDatosJSON()

*/


