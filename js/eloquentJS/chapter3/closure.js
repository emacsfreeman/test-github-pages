/*
  The ability to treat functions as values, combined with the fact that localbindings are re-created 
  every time a function is called, brings up an interestingquestion. What happens to local bindings 
  when the function call that createdthem is no longer active?The following code shows an example of 
  this. It defines a function,wrapValue,that creates a local binding. It then returns a function that 
  accesses and returnsthis local binding.
*/

function wrapValue(n)
{
  let local = n;
  return () => local;
}

let wrap1 = wrapValue("blabla");
let wrap2 = wrapValue(2);

console.log(wrap1());
console.log(wrap2());

/* 
  This is allowed and works as you’d hope—both instances of the binding canstill be accessed. 
  This situation is a good demonstration of the fact that localbindings are created anew for 
  every call, and different calls can’t trample onone another’s local bindings.This feature—being 
  able to reference a specific instance of a local binding inan enclosing scope—is calledclosure. 
  A function that references bindings fromlocal scopes around it is calledaclosure. This behavior 
  not only frees you fromhaving to worry about lifetimes of bindings but also makes it possible 
  to usefunction values in some creative ways.With a slight change, we can turn the previous 
  example into a way to createfunctions that multiply by an arbitrary amount.
*/

function multiplier(factor)
{
  return number => number * factor;
}

let twice = multiplier(2);
console.log(twice(5));

/* 
  The explicitlocalbinding from thewrapValueexample isn’t really neededsince a parameter is itself 
  a local binding.Thinking about programs like this takes some practice. A good mental modelis to 
  think of function values as containing both the code in their body and theenvironment in which 
  they are created. When called, the function body seesthe environment in which it was created, 
  not the environment in which it iscalled.In the example,multiplieris called and creates an 
  environment in which itsfactorparameter is bound to 2. The function value it returns, which 
  is storedintwice, remembers this environment. So when that is called, it multiplies itsargument 
  by 2.
*/



