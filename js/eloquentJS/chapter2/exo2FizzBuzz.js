for (let i = 0; i < 100; i++) 
{
  if (i % 3 == 0 && i % 5 != 0) 
  {
    console.log('Fizz because i = ' + i + ' so i % 3 == 0 AND i % 5 != 0');
  }
  else if (i % 3 != 0 && i % 5 == 0) 
  {
    console.log('Buzz because i = ' + i + ' so i % 5 == 0 AND i % 3 != 0');
  }
  else if (i % 15 == 0) 
  {
    console.log('FizzBuzz because i = ' + i + ' so i % 15 == 0');
  }
}
