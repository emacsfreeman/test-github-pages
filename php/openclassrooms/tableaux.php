<?php

$prenoms[0] = 'Laurent';
$prenoms[1] = 'Stéphane';
$prenoms[2] = 'Francis';

echo '<p>Je m\'appelle ' . $prenoms[0] . '</p>';

$prenom2 = array('Anna', 'Loranovna', 'Josetta', 'Esa');
echo '<p>Elle s\'appelle ' . $prenom2[0] . '</p>';

$personne = array('nom' => 'Garnier', 'prenom' => 'Laurent', 'age' => 36);
print_r($personne);
?>
<h2>Avec une boucle for</h2>
<?php
for ($numero=0; $numero < 3; $numero++)
{
  echo '<p>' . $prenoms[$numero] . '</p>';
}
?>
<h2>Avec une boucle foreach</h2>
<?php
foreach ($personne as $libelle => $detail)
{
  echo '<p>'. $libelle . ' : ' . $detail . '</p>';
}

 ?>
