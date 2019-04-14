function greetVisitor(phrase) {
  var welcome = phrase + ". Content de vous voir !<br><br>"; // Variable locale
  var sayWelcome = function () {
    document.getElementById("greeting").innerHTML += welcome;
  }
  return sayWelcome;
}

var personalGreeting = greetVisitor("Bienvenue, ami");
personalGreeting(); // affiche "Bienvenue, ami. Content de vous voir !"
