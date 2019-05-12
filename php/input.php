<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <form action="site.php" method="get">
      Name: <input type="text" name="username">
      <br>
      Age: <input type="number" name="userage">
      <input type="submit">
    </form>
    <br>

    Your name is: <?php echo $_GET["username"]; ?>
    <br>
    Your age is: <?php echo $_GET["userage"]; ?>
  </body>
</html>
