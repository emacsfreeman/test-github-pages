<?php

$adulte = true;

if ($adulte)
{
  ?>
  <p>Tu es un adulte</p>
<?php
}

$age = 4;
switch ($age) {
  case 4:
  ?>
    <p>Tu as 4 ans</p>
  <?php
    break;
  case 18:
    echo "Tu as 18 ans";
    break;
  default:
    echo "Tu as n'importe quel âge sauf 4 ou 18 ans.";
    break;
}

 ?>
