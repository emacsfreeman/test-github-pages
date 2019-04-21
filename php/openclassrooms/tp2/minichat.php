<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Mini-chat</title>
    <style media="screen">
      form
      {
        text-align: center;
      }
    </style>
  </head>
  <body>
    <form action="minichat_post.php" method="post">
      <p>
          <label>Pseudo : <input type="text" name="pseudo" id="pseudo"></label>
          <br>
          <label>Message : <input type="textarea" name="message"></label>
          <br>
          <input type="submit" value="Envoyer">
      </p>
    </form>

    <?php
    // Connexion à la base de données
    try
    {
        $bdd = new PDO('mysql:host=localhost;dbname=minichat', 'root', '');
    }
    catch(Exception $e)
    {
      die('Erreur : '.$e -> getMessage());
    }

    // Récupération des 10 derniers messages
    $reponse = $bdd -> query('SELECT pseudo, message FROM visiteurs ORDER BY ID DESC LIMIT 0, 10');
    // Affichage de chaque message (toutes les données sont protégées par htmlspecialchars)
    echo '<ol>';
    while ($donnees = $reponse -> fetch())
    {
      echo '<li><strong>' . htmlspecialchars($donnees['pseudo']) . '</strong> : ' . htmlspecialchars($donnees['message']) .'</li>';
    }
    echo '</ol>';

    $reponse -> closeCursor();

     ?>

  </body>
</html>
