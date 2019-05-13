<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>


    <form action="site.php" method="post">
      What's your grade?<br>
      <input type="text" name="grade"><br>
      <input type="submit">
    </form>

    <?php

      $grade = $_POST["grade"];
      switch($grade){
        case "A":
          echo "You did amazing";
          break;
        case "B":
          echo "You did pretty well";
          break;
        case "C":
          echo "You did poorly";
          break;
        case "D":
          echo "You did very poorly";
          break;
        case "F":
          echo "YOU FAIL!";
          break;
        default:
          echo "Invalid grade!";
      }

     ?>

  </body>
</html>
