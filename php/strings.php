<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <?php

      $phrase = "Bitcoin Academy";
      echo "<p>" .strtoupper($phrase)."</p>";
      echo "<ol>";
      echo "<li>$phrase[0]</li>";
      echo "<li>$phrase[1]</li>";
      echo "<li>$phrase[2]</li>";
      echo "</ol>";
      echo str_replace("Bitcoin", "Ethereum", $phrase);

    ?>

  </body>
</html>
