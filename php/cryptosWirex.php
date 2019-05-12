<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <h1>Crypto disponible sur <a href="https://bit.ly/2QgCLRH" target="_blank">Wirex</a> </h1>
    <form action="site.php" method="post">
      <a href="https://coinmarketcap.com/currencies/bitcoin/" target="_blank">Bitcoin</a>: <input type="checkbox" name="cryptos[]" value="<a href='https://coinmarketcap.com/currencies/bitcoin/' target='_blank'>Bitcoin</a>">
      <br>
      <a href="https://coinmarketcap.com/currencies/ethereum/" target="_blank">Ethereum</a>: <input type="checkbox" name="cryptos[]" value='<a href="https://coinmarketcap.com/currencies/ethereum/" target="_blank">Ethereum</a>'>
      <br>
      <a href="https://coinmarketcap.com/currencies/litecoin/" target="_blank">Litecoin</a>: <input type="checkbox" name="cryptos[]" value='<a href="https://coinmarketcap.com/currencies/litecoin/" target="_blank">Litecoin</a>'>
      <br>
      <a href="https://coinmarketcap.com/currencies/ripple/" target="_blank">XRP</a>: <input type="checkbox" name="cryptos[]" value='<a href="https://coinmarketcap.com/currencies/ripple/" target="_blank">XRP</a>'>
      <br>
      <a href="https://coinmarketcap.com/currencies/stellar/" target="_blank">Stellar</a>: <input type="checkbox" name="cryptos[]" value='<a href="https://coinmarketcap.com/currencies/stellar/" target="_blank">Stellar</a>'>
      <br>
      <a href="https://coinmarketcap.com/currencies/waves/" target="_blank">Waves</a>: <input type="checkbox" name="cryptos[]" value='<a href="https://coinmarketcap.com/currencies/waves/" target="_blank">Waves</a>'>
      <br>
      <a href="https://coinmarketcap.com/currencies/nano/" target="_blank">Nano</a>: <input type="checkbox" name="cryptos[]" value='<a href="https://coinmarketcap.com/currencies/nano/" target="_blank">Nano</a>'>
      <br>
      <a href="https://coinmarketcap.com/currencies/dai/" target="_blank">Dai</a>: <input type="checkbox" name="cryptos[]" value='<a href="https://coinmarketcap.com/currencies/dai/" target="_blank">Dai</a>'>
      <br>
      <a href="https://coinmarketcap.com/currencies/wollo/" target="_blank">Wollo</a>: <input type="checkbox" name="cryptos[]" value='<a href="https://coinmarketcap.com/currencies/wollo/" target="_blank">Wollo</a>'>
      <br>
      <input type="submit">
    </form>

    <?php

        echo "<h2>Cryptos sélectionnées</h2>";

        $cryptos = $_POST["cryptos"];
        echo "<ol>";
        for ($i=0; $i < count($cryptos); $i++) {
          echo "<li>" . $cryptos[$i] . "</li>";
        }
        echo "</ol>";


     ?>

  </body>
</html>
