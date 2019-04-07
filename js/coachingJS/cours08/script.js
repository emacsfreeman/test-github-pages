var nom1;
var nom2;
var nom3;
var techno;

document.getElementById('ModifierListe').onclick = saisirListe;

function saisirListe() {
  techno = prompt("Saisir la techno (Back ou Front) :");
  nom1 = prompt("Saisir le langage 1 : ");
  nom2 = prompt("Saisir le langage 2 : ");
  nom3 = prompt("Saisir le langage 3 : ");
  actualiserListe();
}

function actualiserListe() {
  document.getElementById("tech").innerHTML = techno;
  document.getElementById("langage1").innerHTML = nom1;
  document.getElementById("langage2").innerHTML = nom2;
  document.getElementById("langage3").innerHTML = nom3;
}
