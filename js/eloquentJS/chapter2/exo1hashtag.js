// Version 1 : "naive" version with 2 variables
let nbHashTag = 0; 
let string = "";
while (nbHashTag < 7)
{
  string += '#';
  console.log(string);
  nbHashTag += 1;
}

// Version 2 : "elegant" version with a property
let string = "";
while (string.length < 7)
{
  string += '#';
  console.log(string);
}

