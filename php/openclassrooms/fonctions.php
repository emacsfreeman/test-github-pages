
<?php

$phrase = 'Bonjour je suis une phrase en français.';
$nombreDeCaracteres = strlen($phrase);

echo '<h2>Il y a ' . $nombreDeCaracteres . ' caractères dans la phrase : &laquo; ' . $phrase . ' &raquo;.</h2>';

function str_shuffle_unicode($str)
{
  $tmp = preg_split("//u", $str, -1, PREG_SPLIT_NO_EMPTY);
  shuffle($tmp);
  return join("", $tmp);
}

echo '<p>Voir la <a href="https://www.php.net/manual/fr/function.str-shuffle.php" target="_blank">documentation</a> pour plus de détails</p>';

echo '<h2>Avec ces mêmes caractères on peut produire la chaîne de caractères : &laquo; ' . str_shuffle_unicode('Ma phrase à mélanger.') . ' &raquo;.</h2>';

echo '<h1>Aujourd\'hui nous sommes le ' . date('d') . '/' . date('m') . '/' . date('Y') . '</h1>';

function direBonjour($nom)
{
  echo '<p>Bonjour ' . $nom . '</p>';
}

direBonjour('Laurent');

 ?>
