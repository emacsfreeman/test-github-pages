// without parameter
const makeNoise = function()
{
  console.log("Pling!");
}
makeNoise();

// with 2 parameters
const power = function(base, exponent)
{
  let result = 1;
  for (let count = 0; count < exponent; count++)
  {
    result *= base;
  }
  return result;
};
console.log(power(2, 10));
