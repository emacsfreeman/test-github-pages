factorial(n)
{
  if (n == 0)
  {
    return 1;
  }
  else 
  {
    return factorial(n - 1) * n;
  }
}

for (var i = 0; i <= 10; i++)
{
  console.log(factorial(i));
}
