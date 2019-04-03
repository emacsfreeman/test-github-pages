// TYPES
// Boolean
<?php
  $logique = True;
  echo "La variable logique renvoie '$logique' lorsqu'elle vaut True.\n";
  $logique = False;
  echo "Elle renvoie '$logique' lorsqu'elle vaut False.\n";
?>

// CONDITIONALS
<?php
  $real_coding = TRUE;
  if ($real_coding == TRUE) {
    echo "<p>Coding is great, but it's hard!<p>\n";
  };
?>

// INTEGERS AND FLOAT
<?php
  $number1 = 1;
  $number2 = 2;
  $number3 = 3;

  $a = $number1 + $number2;
  echo "$number1 + $number2 = $a\n";
  $a = $number3 - $number2;
  echo "$number3 - $number2 = $a\n";
  $a = $number2 * $number3;
  echo "$number2 x $number3 = $a\n";
  $a = $number3 / $number2;
  echo "$number3 / $number2 = $a is not an integer! It's a float.\n";
  $a = $number3 % $number2;
  echo "$number3 mod $number2 = $a\n";
?>

// STRINGS
<?php
  echo 'This is a simple string.\n' . "\n";

  echo 'Arnold once said: "I\'ll be back!".' . "\n";
?>

// ARRAYS
<?php
  $array = array(
    "gauche" => "droite",
    "haut"   => "bas",
    "clé"    => "valeur",
    2        => "a",
    "3"      => 2,
    true     => "vrai",
  );
  var_dump($array);
  var_dump($array["gauche"]);
  var_dump($array[2]);
  var_dump($array["3"]);
  var_dump($array[true]);
?>

// FUNCTIONS
<?php
  function writeMessage($message = 'Hello World') {
    return "$message\n";
  }

  echo writeMessage('Goodbye');
  ?>

  // LOOPS
  <?php
  for ($i = 0; $i < 10; $i++) {
    echo 'Number ' .$i.'<br>';
  }
  ?>
