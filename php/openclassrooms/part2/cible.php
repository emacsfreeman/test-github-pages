<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Page cible</title>
  </head>
  <body>
    <p>Bonjour <?php echo htmlspecialchars($_POST['prenom']); ?> </p>
    <?php
    if (isset($_POST['vegetarien']))
    {
      echo '<p>Vous êtes donc végétarien.</p>';
    }
    else
    {
      echo '<p>Vous n\'êtes pas végétarien.</p>';
    }
     ?>
  </body>
</html>
