let theNumber = Number(prompt("Pick a number"));
if (!Number.isNaN(theNumber)) 
{
  console.log("Your number is the square root of " +theNumber * theNumber);
  if (theNumber < 10)
  {
    console.log("Small");
  }
  else if (theNumber < 100)
  {
    console.log("Medium");
  }
  else
  {
    console.log("Large");
  }
}
else
{
  console.log("Hey! Why didn't you give me a number?");
}
