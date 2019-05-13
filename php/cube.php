<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <form action="site.php" method="post">
      Choose a (whole) number: <input type="number" name="number">
      <br>
      <input type="submit">
    </form>

    <?php

        function cube($number){
          return $number * $number * $number;
        }

        $number = $_POST["number"];
        echo "<p>You choose: " . $number ."</p>";
        $cubeResult = cube($number);
        echo "<p>And here is its cube: ". $cubeResult . "</p>";

     ?>

  </body>
</html>
