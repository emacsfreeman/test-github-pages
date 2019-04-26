function isEven(n)
{
    if (n == 0) return true;
    else if (n == 1) return false;
    else if (n < 0) return isEven(-n);
    else return isEven(n - 2);
}

// Test
for (let i = 0; i < 10; i++)
{
  if (isEven(i)) console.log("i = " + i + " is even");
  else console.log("i = " + i + " is odd");
}

