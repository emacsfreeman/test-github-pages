let x = 10;
if (true)
{
  let y = 20;
  let z = 30;
  console.log(x + y + z);
}

// y is not visible here
console.log(x + z);
