<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>


    <?php

      $cryptos = array("Bitcoin", 7124.77, "Ethereum", 189.16);
      echo "<p>" . $cryptos[0] . "a pour valeur actuellement : " . $cryptos[1] . "$</p>";
      $cryptos[1] = "<p><strong>ça change tout le temps en fait !</strong></p>";
      echo $cryptos[1];
      echo "<p>Ce tableau a : " . count($cryptos) . " éléments</p>";

     ?>

  </body>
</html>
