<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Mon super site</title>
  </head>
  <body>
    <p>
      <?php
      if (isset($_GET['nom']) AND isset($_GET['prenom']) AND isset($_GET['repeter']))
      {
        $nbRepetitions = (int) $_GET['repeter'];
        if ($nbRepetitions < 100)
        {
          for ($repetition=0; $repetition < $nbRepetitions; $repetition++)
          {
            echo '<p>Bonjour ' . $_GET['nom'] . ' ' . $_GET['prenom'] . '</p>';
          }
        }
        elseif ($nbRepetitions >= 100)
        {
          echo '<h1>Nombre de répétitions trop important.</h1>';
        }
        elseif ($nbRepetitions < 1)
        {
          echo '<h1>Nombre de répétition inférieur à 1 donc problème.</h1>';
        }
        else
        {
          echo '<h1>What The Fuck?!</h1>';
        }
      }
      else
      {
        echo 'Pas de nom ou de prénom défini !';
      }
      ?>

    </p>
  </body>
</html>
