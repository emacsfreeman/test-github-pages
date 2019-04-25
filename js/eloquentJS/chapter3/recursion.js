/* 
  It is perfectly okay for a function to call itself, as long as it doesn’t do it sooften that it overflows the stack. 
  A function that calls itself is called recursive. Recursion allows some functions to be written in a different style. 
  Take, for example, this alternative implementation of power:
*/


function power(base, exponent)
{
  if (exponent == 0)
  {
    return 1;
  }
  else 
  {
    return base * power(base, exponent - 1);
  }
}

console.log(power(2, 4));


/* 
  This is rather close to the way mathematicians define exponentiation and arguably describes the concept more clearly than 
  the looping variant.  Thefunction calls itself multiple times with ever smaller exponents to achieve the repeated 
  multiplication. But this implementation has one problem: in typical JavaScript implementations, it’s about three times 
  slower than the looping version. Running througha simple loop is generally cheaper than calling a function multiple times.
  The dilemma of speed versus elegance is an interesting one. You can see it asa kind of continuum between human-friendliness 
  and machine-friendliness. Al-most any program can be made faster by making it bigger and more convoluted. The programmer 
  has to decide on an appropriate balance.
*/

function findSolution(target)
{
    function find(current, history) 
    {
        if (current == target) 
        {
            return history;
        }
        else if (current > target)
        {
            return null;
        }
        else 
        {
            return find(current + 5, `(${history} + 5)`) || find(current * 3, `(${history} * 3)`);
        }
    }
    return find(1, "1");
}
// tests
for (let i = 0; i < 100; i++)
{
  console.log('Pour i = ' + i + ', on a :')
  console.log('------------------')
  console.log(findSolution(i));
  console.log('======================================');
}

/* 
  Note that this program doesn’t necessarily find theshortestsequence of op-erations. 
  It is satisfied when it finds any sequence at all.It is okay if you don’t see how 
  it works right away. Let’s work through it,since it makes for a great exercise in 
  recursive thinking.The inner functionfinddoes the actual recursing. It takes two 
  arguments: the current number and a string that records how we reached this number. 
  If it finds a solution, it returns a string that shows how to get to the target. 
  If no solution can be found starting from this number, it returnsnull.To do this, 
  the function performs one of three actions. If the current numberis the target number, 
  the current history is a way to reach that target, so itis returned. If the current 
  number is greater than the target, there’s no sensein further exploring this branch 
  because both adding and multiplying will only make the number bigger, so it returnsnull. 
  Finally, if we’re still below thetarget number, the function tries both possible paths that 
  start from the currentnumber by calling itself twice, once for addition and once for multiplication. 
  If the first call returns something that is notnull, it is returned. Otherwise, thesecond call is 
  returned, regardless of whether it produces a string ornull. To better understand how this function 
  produces the effect we’re looking for,let’s look at all the calls tofindthat are made when searching 
  for a solutionfor the number 13.
*/

document.write('<p>Pour aller plus loin :</p>');
document.write('<ul>');
document.write('<li><a href="https://codeburst.io/learn-and-understand-recursion-in-javascript-b588218e87ea" target="_blank">Codeburst.io</a></li>');
document.write('<li><a href="https://javascript.info/recursion" target="_blank">javascript.info</a></li>');
document.write('<li><a href="https://dev.to/ryanfarney3/intro-to-recursion-in-js-32g" target="_blank">ryan farney</a></li>');
document.write('<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#Recursion" target="_blank">MDN</a></li>');
document.write('</ul>');


