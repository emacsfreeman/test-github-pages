var nom1;
var nom2;
var nom3;
var techno;

document.getElementById('ModifierListe').onclick = saisirListe; 

function saisirListe() {
  techno = prompt("Saisir la techno (Back ou Front) :");
  if (techno.toLowerCase() === 'back') {
    techno = '<a href="https://en.wikipedia.org/wiki/Front_and_back_ends#Back-end_focused" target="_blank">Back</a>';
  }
  else if (techno.toLowerCase() === 'front') {
    techno = '<a href="https://en.wikipedia.org/wiki/Front_and_back_ends#Front-end_focused" target="_blank">Front</a>';
  }
  nom1 = prompt("Saisir le langage 1 : ");
  if (nom1.toUpperCase() === 'HTML') {
    nom1 = '<a href="https://fr.wikipedia.org/wiki/HTML5" target="_blank">HTML 5</a>'
  }
  else if (nom1.toUpperCase() === 'PHP') {
    nom1 = '<a href="https://fr.wikipedia.org/wiki/PHP" target="_blank">PHP 7</a>';
  }

  nom2 = prompt("Saisir le langage 2 : ");
  if (nom2.toUpperCase() === 'CSS') {
    nom2 = '<a href="https://en.wikipedia.org/wiki/Cascading_Style_Sheets" target="_blank">CSS 3</a>'
  }
  else if (nom2.toUpperCase() === 'PYTHON') {
    nom2 = '<a href="https://fr.wikipedia.org/wiki/Python_(langage)" target="_blank">Python 3</a> avec <a href="https://www.djangoproject.com/" target="_blank">Django</a> ou <a href="http://flask.pocoo.org/" target="_blank">Flask</a>';
  }

  nom3 = prompt("Saisir le langage 3 : ");
  if (nom3.toUpperCase() === 'JAVASCRIPT') {
    nom3 = '<a href="https://fr.wikipedia.org/wiki/JavaScript" target="_blank">JavaScript</a>'
  }
  else if (nom3.toUpperCase() === 'RUBY') {
    nom3 = '<a href="https://fr.wikipedia.org/wiki/Ruby" target="_blank">Ruby</a> avec <a href="https://fr.wikipedia.org/wiki/Ruby_on_Rails" target="_blank">Rails</a> ou <a href="https://fr.wikipedia.org/wiki/Sinatra_(logiciel)" target="_blank">Sinatra</a>';
  }

  actualiserListe();
}

function actualiserListe() {
  document.getElementById("tech").innerHTML = techno;
  document.getElementById("langage1").innerHTML = nom1;
  document.getElementById("langage2").innerHTML = nom2;
  document.getElementById("langage3").innerHTML = nom3;
}

