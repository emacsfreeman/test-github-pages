<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <form action="site.php" method="post">
      Password: <input type="password" name="password">
      <br>
      <input type="submit">
    </form>
    <!--
        POST contrairement à GET n'affichera pas
        la valeur dans de la variable dans l'url
      -->
    <br><br>

    <?php

      echo $_POST["password"];

     ?>

  </body>
</html>
