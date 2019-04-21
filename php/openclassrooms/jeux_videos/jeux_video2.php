<?php

  if (isset($_GET['console']))
  {

    $bdd = new PDO('mysql:host=localhost;dbname=testOC', 'root', '', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
    $requete = $bdd -> prepare('SELECT * FROM jeux_video WHERE console=?');
    $requete -> execute(array($_GET['console']));
    while ($donnees = $requete -> fetch())
    {
      echo '<p>' . $donnees['console'] . ' - ' . $donnees['nom'] . ' - ' . $donnees['prix'] .'€</p>';
    }

  }

 ?>
