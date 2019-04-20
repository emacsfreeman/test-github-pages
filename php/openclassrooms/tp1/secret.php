<?php
if (isset($_POST['mdp']) AND $_POST['mdp'] == 'kangourou')
{
  echo '<h1>Voici les codes secrets de la NASA</h1>';
}
else {
  echo '<h1>Vous n\'êtes pas autorisé(e) à accéder à cette page</h1>';
}
 ?>
