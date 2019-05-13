<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>


    <?php

      echo "<h2>Boucle while</h2>";
      $index = 1;
      while($index <= 5){
        echo "$index <br>";
        $index++;
      }

      echo "<hr>";

      echo "<h2>Boucle for</h2>";
      $luckyNumbers = array(4, 8, 14, 16, 23, 42);
      for ($i = 0; $i < count($luckyNumbers); $i++) {
        echo "$luckyNumbers[$i] <br>";
      }

     ?>

  </body>
</html>
