/* 
  There are two more or less natural ways for functions to be introduced intoprograms.
  The first is that you find yourself writing similar code multiple times. 
  You’dprefer not to do that. Having more code means more space for mistakes tohide and 
  more material to read for people trying to understand the program.
  So you take the repeated functionality, find a good name for it, and put it intoa function.
  The second way is that you find you need some functionality that you haven’twritten yet and 
  that sounds like it deserves its own function. You’ll start bynaming the function, and then 
  you’ll write its body.  You might even startwriting code that uses the function before you 
  actually define the functionitself.How difficult it is to find a good name for a function 
  is a good indicationof how clear a concept it is that you’re trying to wrap. Let’s go 
  through anexample.
*/

// Version 1
function printFarmInventory(cows, chickens)
{
    let cowString = String(cows);
    while (cowString.length < 3)
    {
        cowString = "0" + cowString;
    }
    console.log(`${cowString} Cows`);
    let chickenString = String(chickens);
    while (chickenString.length < 3)
    {
        chickenString = "0" + chickenString;
    }
    console.log(`${chickenString} Chickens`);
}

printFarmInventory(7, 11);

/* 
  Writing .length after a string expression will give us the length of that string.
  Thus, thewhileloops keep adding zeros in front of the number strings untilthey 
  are at least three characters long.Mission accomplished! But just as we are 
  about to send the farmer the code(along with a hefty invoice), she calls and tells 
  us she’s also started keepingpigs, and couldn’t we please extend the software to 
  also print pigs? We sure can. But just as we’re in the process of copying and 
  pasting those four lines one more time, we stop and reconsider. There has to be a 
  better way.Here’s a first attempt:
*/

// Version 2
function printZeroPaddedWithLabel(number, label)
{
    let numberString = String(number);
    while (numberString.length < 3)
    {
        numberString = "0" + numberString;
    }
    console.log(`${numberString} ${label}`);
}


function printFarmInventory(cows, chickens, pigs)
{
  printZeroPaddedWithLabel(cows, "Cows");
  printZeroPaddedWithLabel(chickens, "Chickens");
  printZeroPaddedWithLabel(pigs, "Pigs");
}

printFarmInventory(7, 11, 3);


/* 
  It works! But that name,printZeroPaddedWithLabel, is a little awkward.
  It conflates three things—printing, zero-padding, and adding a label—into 
  asingle function. Instead of lifting out the repeated part of our program 
  wholesale, let’s tryto pick out a single concept.
*/

// Version 3
function zeroPad(number, width)
{
    let string = String(number);
    while (string.length < width)
    {
        string = "0" + string;
    }
    return string;
}

function printFarmInventory(cows, chickens, pigs) 
{
    console.log(`${zeroPad(cows, 3)} Cows`);
    console.log(`${zeroPad(chickens, 3)} Chickens`);
    console.log(`${zeroPad(pigs, 3)} Pigs`);
}

printFarmInventory(7, 16, 3);

/* 
  A function with a nice, obvious name likezeroPadmakes it easier for someonewho reads the code to figure out what it does. 
  And such a function is useful in more situations than just this specific program.
*/

document.write('<h2>Pour aller plus loin :</h2>');
document.write('<ul>');
document.write('<li><a href="https://codeburst.io/all-about-javascript-functions-in-1-article-49bfd94b31ab" target="_blank">codeburst.io</a></li>');
document.write('<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions" target="_blank">MDN</a></li>');
document.write('<li><a href="https://medium.com/javascript-scene/the-two-pillars-of-javascript-pt-2-functional-programming-a63aa53a41a4" target="_blank">Eric Elliot</a></li>');
document.write('<li><a href="https://bonsaiden.github.io/JavaScript-Garden/" target="_blank">JS Garden</a></li>');
document.write('</ul>');


