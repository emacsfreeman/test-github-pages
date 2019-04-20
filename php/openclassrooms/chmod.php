<?php

  // 1 : on ouvre le fichier
  $monfichier = fopen('compteur.txt', 'r+');

  // 2 : on fera ici nos opérations sur le fichier...

  // 3 : quand on a fini de l'utiliser, on ferme le fichiers
  fclose($monfichier);

 ?>

<ul>
  <li>r : ouvre le fichier en lecture seule. Cela signifie que vous pourrez seulement lire le fichier.</li>
  <li>r+ : ouvre le fichier en lecture et écriture. Vous pourrez non seulement lire le fichier, mais aussi y écrire (on l'utilisera souvent en pratique)</li>
  <li>a : ouvre le fichier en écriture seule. Mais il y a un avantage : si le fichier n'existe pas, il est automatiquement créé.</li>
  <li>a+ : ouvre le fichier en lecture et écriture. Si le fichier n'existe pas, il est créé automatiquement. Attention : le répertoire doit avoir un CHMOD à 777 dans ce cas ! À noter que si le fichier existe déjà, le texte sera rajouté à la fin.</li>
</ul>

<?php
// 1 : on ouvre le fichier
$monfichier = fopen('compteur.txt', 'r+');

// 2 : on lit la première ligne du fichier
$ligne = fgets($monfichier);

// 3 : quand on a fini de l'utiliser, on ferme le fichier
fclose($monfichier);
?>

<?php fputs($monfichier, 'Texte à écrire'); ?>

<?php
$monfichier = fopen('compteur.txt', 'r+');

$pages_vues = fgets($monfichier); // On lit la première ligne (nombre de pages vues)
$pages_vues += 1; // On augmente de 1 ce nombre de pages vues
fseek($monfichier, 0); // On remet le curseur au début du fichier
fputs($monfichier, $pages_vues); // On écrit le nouveau nombre de pages vues

fclose($monfichier);

echo '<p>Cette page a été vue ' . $pages_vues . ' fois !</p>';
?>
