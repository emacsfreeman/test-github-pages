function min(a, b)
{
  if (typeof a != "number" || typeof b != "number")
  {
    console.log("Type error, a AND b must be numbers!");
  }
  else
  {
    if (a < b) return a;
    else return b;
  }
}

// Test type error
min("a", 3);
min(2, "b");

// Test numbers
console.log("min(2, 3) = " + min(2, 3));
console.log("min(5, 4) = " + min(5, 4));
