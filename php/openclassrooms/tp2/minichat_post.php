<?php
// Connexion à la base de données
try
{
  $bdd = new PDO('mysql:host=localhost;dbname=minichat;charset=utf8', 'root', '');
}
catch(Exception $e)
{
  die('Erreur : '.$e -> getMessage());
}
// Effectuer ici la requête qui insère le message
$requete = $bdd -> prepare('INSERT INTO visiteurs(pseudo, message) VALUES(?, ?)');
$requete -> execute(array($_POST['pseudo'], $_POST['message']));

// Puis rediriger vers minichat.php comme ceci :
header('Location: minichat.php');

?>
