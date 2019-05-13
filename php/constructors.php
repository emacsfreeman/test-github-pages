<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>


    <?php

      class Book {
        var $title;
        var $author;
        var $pages;
        var $year;
        var $whereToBuyIt;

        function __construct($aTitle, $aAuthor, $aPages, $aYear, $aWhereToBuyIt){
          $this->title = $aTitle;
          $this->author = $aAuthor;
          $this->pages = $aPages;
          $this->year = $aYear;
          $this->whereToBuyIt = $aWhereToBuyIt;

        }
      }

      $book1 = new Book(
        "Harry Potter",
        "JK Rowling",
        320,
        1997,
        '<a href="https://amzn.to/2Hizvl8" target="_blank" >Harry Potter</a>'
      );

      $book2 = new Book(
        "Lord of the Rings",
        "Tolkien",
        1135,
        1998,
        '<a href="https://amzn.to/2JADZ9v" target="_blank" >Lord of the Rings</a>'
      );


      echo "<ol>";

      echo "<li><p><u>First book</u></p><ul>";
      echo "<li><strong>Title:</strong> " . $book1->title . "</li>";
      echo "<li><strong>Author:</strong> " . $book1->author . "</li>";
      echo "<li><strong>Number of pages:</strong> " . $book1->pages . "</li>";
      echo "<li><strong>Year of publishing:</strong> " . $book1->year . "</li>";
      echo "<li><strong>Buy it on Amazon:</strong> " . $book1->whereToBuyIt . "</li>";
      echo "</ul></li>";

      echo "<li><p><u>Second book</u></p><ul>";
      echo "<li><strong>Title:</strong> " . $book2->title . "</li>";
      echo "<li><strong>Author:</strong> " . $book2->author . "</li>";
      echo "<li><strong>Number of pages:</strong> " . $book2->pages . "</li>";
      echo "<li><strong>Year of publishing:</strong> " . $book2->year . "</li>";
      echo "<li><strong>Buy it on Amazon:</strong> " . $book2->whereToBuyIt . "</li>";
      echo "</ul></li>";

      echo "</ol>";



      ?>



  </body>
</html>
