function greet(who) 
{
  console.log("Hello " + who);
}
greet("Harry");
console.log("Bye");

/* 
  Because a function has to jump back to the place that called it when it re-turns, the computer must remember the context 
  from which the call happened.In one case,console.loghas to return to thegreetfunction when it is done.In the other case, 
  it returns to the end of the program.The place where the computer stores this context is thecall stack. Everytime a function 
  is called, the current context is stored on top of this stack.When a function returns, it removes the top context from the 
  stack and usesthat context to continue execution.Storing this stack requires space in the computer’s memory. When the 
  stackgrows too big, the computer will fail with a message like “out of stack space”or “too much recursion”.  The following 
  code illustrates this by asking thecomputer a really hard question that causes an infinite back-and-forth betweentwo 
  functions.  Rather, itwouldbe infinite, if the computer had an infinitestack. As it is, we will run out of space, or 
  “blow the stack”.
*/


// bug
function chicken() { return egg(); }
function egg() { return chicken(); }
console.log(chicken() + " came first.");

