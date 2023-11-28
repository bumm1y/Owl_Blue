let indicePregunta = 0;
let btn_correspondiente = [
  document.getElementById("btn1"), 
  document.getElementById("btn2"),
  document.getElementById("btn3"),
  document.getElementById("btn4"), 
];
let respuestasCorrectas = 0;

function redirigir(url){
  window.location.href = url;
}


function botonSiguiente() {
  document.getElementById("continuar").style.display = "block";
}

function oprimir(indice, alternativas, respuesta) {
  console.log(alternativas);
  if (alternativas[indice]==respuesta) {
    respuestasCorrectas++;
    btn_correspondiente[indice].style.background = "lightgreen";
    document.getElementById("btn1").removeEventListener("click", function () {
      oprimir(0, alternativas, respuesta)});
    document.getElementById("btn2").removeEventListener("click", function () {
      oprimir(1, alternativas, respuesta)});
    document.getElementById("btn3").removeEventListener("click", function () {
      oprimir(2, alternativas, respuesta)});
    document.getElementById("btn4").removeEventListener("click", function () {
      oprimir(3, alternativas, respuesta)});
    
  }else{
    btn_correspondiente[indice].style.background = "pink";
    document.getElementById("btn1").removeEventListener("click", function () {
      oprimir(0, alternativas, respuesta)});
    document.getElementById("btn2").removeEventListener("click", function () {
      oprimir(1, alternativas, respuesta)});
    document.getElementById("btn3").removeEventListener("click", function () {
      oprimir(2, alternativas, respuesta)});
    document.getElementById("btn4").removeEventListener("click", function () {
      oprimir(3, alternativas, respuesta)});
  }
  setTimeout(() => {
    reiniciar();
    botonSiguiente();
  }, 3000);
}

function reiniciar(){
  for (const btn of btn_correspondiente) {
    btn.style.background = "white";
  }
}
  


function mostrar(elemento, mensaje) {
  return document.getElementById(elemento).innerHTML = mensaje
}

function desordenar(op1, op2, op3, op4) {
  let alternativas = [op1, op2, op3, op4]
  return alternativas.sort(()=>Math.random()-0.5)
}


async function nuevaPregunta(datos) {
  const categoria = datos.actividades[indicePregunta].categoria;
  const pregunta = datos.actividades[indicePregunta].pregunta;
  const video = datos.actividades[indicePregunta].videos;
  const respuesta = datos.actividades[indicePregunta].respuesta;
  const alternativa1 = datos.actividades[indicePregunta].alternativa1;
  const alternativa2 = datos.actividades[indicePregunta].alternativa2;
  const alternativa3 = datos.actividades[indicePregunta].alternativa3;
  let alternativas = desordenar(respuesta, alternativa1, alternativa2, alternativa3);
  console.log(alternativas);
  mostrar("categoria", categoria);
  mostrar("pregunta", pregunta);
  mostrar("video", video);
  mostrar("btn1", alternativas[0]);
  mostrar("btn2", alternativas[1]);
  mostrar("btn3", alternativas[2]);
  mostrar("btn4", alternativas[3]);
  document.getElementById("btn1").addEventListener("click", function () {
    oprimir(0, alternativas, respuesta);
  }, {once: true});
  document.getElementById("btn2").addEventListener("click", function () {
    oprimir(1, alternativas, respuesta);
  }, {once: true});
  document.getElementById("btn3").addEventListener("click", function () {
    oprimir(2, alternativas, respuesta);
  }, {once: true});
  document.getElementById("btn4").addEventListener("click", function () {
    oprimir(3, alternativas, respuesta);
  }, {once: true});
}
  
async function obtenerJSON() {
  var ruta = '/acts/' + categoria + '/capsula0/lessons/lessonJSON';   
  return fetch(ruta)
    .then(response => {
      if (response.ok) {
        return response.json();
      }
    })
    .catch(error => {
      console.error('Error en la solicitud:', error);
    });
}

function cambiarPregunta() {
  document.getElementById("continuar").style.display = "none";
  obtenerJSON().then((datos) => {
    if (indicePregunta < datos.actividades.length) {
      nuevaPregunta(datos);
      indicePregunta++;
    } else {
      if (respuestasCorrectas == 5) {
        redirigir('http://127.0.0.1:8000/'+ categoria +'/completelesson/');
      } else {
        redirigir('http://127.0.0.1:8000/' + categoria + '/failedlesson/');
      }
    }
  });
}

document.getElementById("continuar").addEventListener("click", cambiarPregunta());


  

