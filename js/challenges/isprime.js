// Return true if n is prime
function isPrime(n) 
{
    // Check if n is less than 2 => not prime
    if (n<2) return false;

    // Loop from 2 to square root of n
    for (let i = 2; i <= Math.sqrt(n); i++) 
        // If i is a divisor of n, n is not prime
        if (n % i == 0) return false;

    return true;
}

for (var i = 0; i < 1000; i++) {
  if (isPrime(i)) {
    document.write("<p style='color:green'>" + i + " est premier</p>");
  }
  else {
    document.write("<p style='color:red'>" + i + " n'est pas premier</p>");
  }
}
