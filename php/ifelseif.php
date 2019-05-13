<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>


    <?php

      $isMale = true;
      $isTall = false;
      if ($isMale && $isTall) {
        echo "<p>You are a tall male</p>";
      } elseif ($isMale && !$isTall) {
        echo "<p>You are male but not tall</p>";
      } elseif (!$isMale && $isTall) {
        echo "<p>You are not male but tall</p>;"
      } else {
        echo "<p>You are not male and not tall</p>";
      }

     ?>

  </body>
</html>
