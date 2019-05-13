<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>


    <h1>Cryptocurrencies available on <a href="https://bit.ly/2QgCLRH" target="_blank">Wirex</a> </h1>
    <?php

        function wirex($name, $coinmarketcap){
          echo "<p>There is $name, and you can check info on coinmarketcap: $coinmarketcap</p>";
        }

        wirex("Bitcoin", '<a href="https://coinmarketcap.com/currencies/bitcoin/" target="_blank">BTC</a>');
        wirex("Ethereum", '<a href="https://coinmarketcap.com/currencies/ethereum/" target="_blank">ETH</a>');

     ?>

  </body>
</html>
