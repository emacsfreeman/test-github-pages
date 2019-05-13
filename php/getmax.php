<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>


    <?php

      function getMax($num1, $num2){
        if ($num1 > $num2) {
          return $num1;
        } elseif ($num2 > $num1) {
          return $num2;
        } else {
          echo "<p>The two numbers are equal</p>";
          return $num1;
        }
      }

      echo getMax(3, 5);
      echo getMax(5, 4);
      echo getMax(3,3);

     ?>

  </body>
</html>
