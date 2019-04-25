// Version 1 : version << naïve >> utilisant 2 variables
let nbHashTag = 0; 
let string = "";
while (nbHashTag < 7)
{
  string += '#';
  console.log(string);
  nbHashTag += 1;
}

// Version 2 : version << élégante >> utilisant une propriété
let string = "";
while (string.length < 7)
{
  string += '#';
  console.log(string);
}

