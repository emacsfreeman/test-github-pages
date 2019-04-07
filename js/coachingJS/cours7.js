document.write("<h1>Quels sont vos langages de programmation favoris ?</h1>");

var continuer = true;
var choixDuLangage = "JavaScript";

document.write("<h2>Liste de vos langages préférés</h2>");

document.write("<ol>");

while (continuer) {
  choixDuLangage = prompt("Citer 1 de vos langages favoris par ordre de préférence");
  document.write("<li>");
  document.write(choixDuLangage);
  document.write("</li>");
  continuer = prompt('Voulez-vous arrêter ?');
  if (continuer.toUpperCase() === 'OUI') {
    continuer = false;
  }
  else {
    continuer = true;
    alert("Au suivant !");
  }
}

document.write("</ol>");

