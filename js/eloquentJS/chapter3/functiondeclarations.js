////////////
// as value
///////////
let sayHello = function()
{
  console.log("Hello");
}

/////////////////////////
// declaration notation
///////////////////////
function square(x)
{
  return x * x;
}

console.log("The future says:", future());
function future() 
{
  return "You'll never have flying cars";
}
// will work in a script even though the function is defined below the code

/////////////////////
// arrow functions
///////////////////
const power = (base, exponent) => 
{
  let result = 1;
  for (let count = 0; count < exponent; count++) 
  {
    result *= base;
  }
  return result;
}

console.log('2^6 = ' + power(2, 6));

/* 
  The arrow comesafterthe list of parameters and is followed by the function’sbody.   
  It expresses something like “this input (the parameters) produces thisresult (the body)”.
  When there is only one parameter name, you can omit the parenthesesaround the parameter list. 
  If the body is a single expression, rather than ablock in braces, that expression will be returned 
  from the function.
*/
const square1 = (x) => { return x * x; };
const square2 = x => x * x;

// it works without parameter
const horn = () => { console.log("Toot"); };



