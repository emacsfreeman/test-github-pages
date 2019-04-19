<?php

$phrase = 'Bonjour je suis une phrase.';
$nombreDeCaracteres = strlen($phrase);

echo '<h2>Il y a ' . $nombreDeCaracteres . ' caractères dans la phrase : &laquo; ' . $phrase . ' &raquo;.</h2>';

echo '<h2>Avec ces mêmes caractères on peut produire la chaîne de caractères : &laquo; ' . str_shuffle('Ma phrase à mélanger.') . ' &raquo;.</h2>';

echo '<h1>Aujourd\'hui nous sommes le ' . date('d') . '/' . date('m') . '/' . date('Y') . '</h1>';

function direBonjour($nom)
{
  echo '<p>Bonjour ' . $nom . '</p>';
}

direBonjour('Laurent');

 ?>
