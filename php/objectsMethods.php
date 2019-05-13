<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>


    <?php

      class Crypto {
        var $shortName;
        var $fullName;
        var $coinmarketcap;

        function __construct($aShortName, $aFullName, $aCoinmarketcap){
          $this->shortName = $aShortName;
          $this->fullName = $aFullName;
          $this->coinmarketcap = $aCoinmarketcap;
        }

        function describeCrypto() {
          echo "<ul>";
          echo "<li><strong>Short name:</strong> " . $this->shortName . "</li>";
          echo "<li><strong>Full name:</strong> " . $this->fullName . "</li>";
          echo "<li><strong>Coinmarketcap:</strong> " . $this->coinmarketcap . "</li>";
          echo "</ul>";
        }
      }

      $crypto1 = new Crypto(
        "BTC",
        "Bitcoin",
        '<a href="https://coinmarketcap.com/currencies/bitcoin/" target="_blank" >Bitcoin</a>'
      );

      $crypto2 = new Crypto(
        "ETH",
        "Ethereum",
        '<a href="https://coinmarketcap.com/currencies/ethereum/" target="_blank" >Ethereum</a>'
      );


      echo "<ol>";
      echo "<li><p><u>First crypto</u></p>";
      $crypto1->describeCrypto();
      echo "</li>";
      echo "<li><p><u>Second crypto</u></p>";
      $crypto2->describeCrypto() ;
      echo "</li>";
      echo "</ol>";



      ?>



  </body>
</html>
