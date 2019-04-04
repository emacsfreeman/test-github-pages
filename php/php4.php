<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <style media="screen">
      body {
        background-color: #FAEBD7;
      }
      h1 {
        color: #0000FF;
      }
      h2 {
        color: #6495ED;
      }
      h3 {
        color: #008B8B;
      }
      p {
        color: #00008B;
      }
    </style>
  </head>
  <body>
    <?php
      // php -S localhost:8000
      echo("<h1>Strings</h1>");
      echo "<hr>";
      $name = "Laurent";
      var_dump($name);
      echo "<p>Bienvenu sur le site <em>$name</em></p>";

      echo "<h2>Fonctions opérant sur les chaînes</h2>";

      echo "<h3>substr</h3>";
      echo "<p>Les deux dernières lettres de ton prénom sont : ";
      echo "<strong>" . substr($name, 5, 3) . "</strong></p>";

      echo "<h3>strlen</h3>";
      echo "<p>$name contient " . strlen($name) . " caractères</p>";

      echo "<h3>str_word_count</h3>";
      $phrase = "Ceci est un morceau de phrase";
      echo "<p>La phrase \"$phrase\" contient " . str_word_count($phrase) . " mots</p>";

      echo "<h3>strrev</h3>";
      echo "<p>À l'endroit : \"$phrase\"</p>";
      echo "<p>À l'envers : \"". strrev($phrase) . "\"</p>";

      echo "<h3>str_replace</h3>";
      echo "<p>J'ai un petit creux. " . str_replace('phrase', 'gâteau', $phrase) . "</p>";

      echo("<h1>Number</h1>");
      echo "<hr>";


      echo "<h2>Types de nombres</h2>";

      echo("<h3>Integer</h3>");
      $myAge = 36;
      var_dump($myAge);
      echo "<p>Tu as $myAge ans</p>";

      echo("<h3>Float</h3>");
      $sqrt2 = 1.414;
      var_dump($sqrt2);
      echo "<p>La racine carrée de 2 vaut environ $sqrt2</p>";

      echo "<h2>Fonctions opérant sur les nombres</h2>";

      echo "<h3>max</h3>";
      $liste = "3, 5, 2, 9, 6, 7";
      $maxList = max(3, 5, 2, 9, 6, 7);
      echo "<p>Le maximum entre $liste est $maxList</p>";

      echo "<h3>min</h3>";
      $minList = min(3, 5, 2, 9, 6, 7);
      echo "<p>Le minimum entre $liste est $minList</p>";

      echo "<h3>abs</h3>";
      echo "<p>|-5| = " .abs(-5) ."</p>";

      echo "<h3>floor</h3>";
      echo "<p>L'arrondi de π à l'unité inférieure est : " . floor(3.14) . "</p>";

      echo "<h3>ceil</h3>";
      echo "<p>L'arrondi de π à l'unité supérieure est : " . ceil(3.14) . "</p>";

      echo "<h3>rand</h3>";
      echo "<p>Prenons un nombre au hasard, n = " . rand() . "</p>";
      echo "<p>Prenons-en encore un au hasard, m = " . rand() . "</p>";
      echo "<p>Prenons-en un autre, p = " . rand() . "</p>";
      echo "<p>Fixons un intervalle [0,9] d'entier, q = " . rand(0, 9) . "</p>";

      echo "<h3>date</h3>";
      echo "<p>La date du jour est " . date('d/m/Y') . "</p>";
      echo "<p>En notation internationale " . date('Y-m-d'). "</p>";
      $jour = date('l');
      $date = date('d');
      $month = date('M');
      $year = date('Y');
      echo "<p>Today is $jour the $date" . "th of $month $year</p>";
      echo "<p>It's " . date('h:i:sa') . " UTC</p>";

      echo "<h4>Définir un fuseau horaire par défaut</h4>";
      date_default_timezone_set("Europe/Paris");
      echo "<p>It's " . date('G:m') . " in France</p>";

      echo("<h1>Boolean</h1>");
      echo "<hr>";
      $vrai = True;
      var_dump($vrai);
      echo "<p>Les informations délivrées ici sont $vrai</p>";

      echo("<h1>Array</h1>");
      echo "<hr>";
      $myArr = [1, 2, 3, 4, 5, 6];
      var_dump($myArr);


      echo("<h1>NULL</h1>");
      echo "<hr>";
      $myNull = null;
      var_dump($myNull);
     ?>
  </body>
</html>
