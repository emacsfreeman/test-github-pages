function square(x) { return x * x; }
console.log(square(4, true, "hedgehog"));

/*
  We definedsquarewith only one parameter. Yet when we call it with three,the language doesn’t complain. 
  It ignores the extra arguments and computesthe square of the first one.JavaScript is extremely 
  broad-minded about the number of arguments youpass to a function. If you pass too many, the extra ones 
  are ignored. If youpass too few, the missing parameters get assigned the valueundefined.The downside 
  of this is that it is possible—likely, even—that you’ll acciden-tally pass the wrong number of arguments 
  to functions. And no one will tellyou about it.
  The upside is that this behavior can be used to allow a function to be calledwith different numbers of 
  arguments. For example, thisminusfunction tries toimitate the-operator by acting on either one or two 
  arguments:
*/


/* 
  If you write an=operator after a parameter, followed by an expression, thevalue of that expression will 
  replace the argument when it is not given.For example, this version ofpowermakes its second argument optional. 
  If you don’t provide it or pass the valueundefined, it will default to two, and thefunction will behave likesquare.
*/
function minus(a, b) 
{
  if (b === undefined) return -a;
  else return a - b;
}

console.log(minus(10));
console.log(minus(10, 5));


function power(base, exponent)
{
  let result = 1;
  for (let count = 0; count < exponent; count++)
  {
    result *= base;
  }
  return result; 
}

console.log(power(4));
console.log(power(2, 6));
