<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <h1>Crypto disponible sur <a href="https://bit.ly/2QgCLRH" target="_blank">Wirex</a> </h1>

    <form action="site.php" method="post">
      <input type="text" name="crypto">
      <input type="submit">
    </form>

    <?php

        $wirex = array(
          "BTC" => '<a href="https://coinmarketcap.com/currencies/bitcoin/" target="_blank">Bitcoin</a>',
          "ETH" => '<a href="https://coinmarketcap.com/currencies/ethereum/" target="_blank">Ethereum</a>',
          "LTC" => '<a href="https://coinmarketcap.com/currencies/litecoin/" target="_blank">Litecoin</a>',
          "XRP" => '<a href="https://coinmarketcap.com/currencies/ripple/" target="_blank">XRP</a>',
          "Stellar" => '<a href="https://coinmarketcap.com/currencies/stellar/" target="_blank">Stellar</a>',
          "Waves" => '<a href="https://coinmarketcap.com/currencies/waves/" target="_blank">Waves</a>',
          "Nano" => '<a href="https://coinmarketcap.com/currencies/nano/" target="_blank">Nano</a>',
          "Dai" => '<a href="https://coinmarketcap.com/currencies/dai/" target="_blank">Dai</a>',
          "Wollo" => '<a href="https://coinmarketcap.com/currencies/wollo/" target="_blank">Wollo</a>'
        );
        echo $wirex[$_POST["crypto"]];

     ?>

  </body>
</html>
