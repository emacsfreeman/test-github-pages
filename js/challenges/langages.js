document.write("<ol>");
document.write("<li>Web</li>");
document.write("<li>Généraliste</li>");
document.write("</ol>");
alert("Veuillez choisir votre type langage de programmation parmi les deux proposés ci-dessus.");

var typeChoisis = prompt("Votre choix de type : ");

document.write("<h1>Langages de programmation choisis</h1>");

if (typeChoisis == '1') {
  document.write("<ul>");
  document.write("<li>Front End</li>");
  document.write("<li>Back End</li>");
  document.write("</ul>");

  alert("Veuillez choisir entre Front et Back.");
  var webChoisis = prompt("Votre choix entre Front et Back : ");

  if (webChoisis == 'Front') {
    document.write("<ul>");
    document.write("<li>HTML</li>");
    document.write("<li>CSS</li>");
    document.write("<li>JavaScript</li>");
    document.write("</ul>");
    document.write("<p>En Front End <em>pas</em> le choix !");
  }
  else if (webChoisis == 'Back') {
    var langage = "";
    var nbItem = prompt("Combien de langages Back End");
    document.write("<ul>");
    for (var i = 0; i < nbItem; i++) {
      document.write("<li>");
      langage = prompt("Langage n° " + (i+1) + ". Votre choix : ");
      document.write(langage);
      document.write("</li>");
    }
    document.write("</ul>");
    var backChoisis = prompt("Votre choix de back : ");
    document.write("<p>Bravo ! Vous avez choisis " + backChoisis + "</p>");
  }
}
