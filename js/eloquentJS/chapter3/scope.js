let x = 10;
if (true)
{
  let y = 20;
  let z = 30;
  console.log(x + y + z);
}

// y is not visible here
console.log(x + z);

const halve = function(n)
{
  return n / 2;
};

let n = 10;
console.log(halve(100));
console.log(n);

// Nested scope 
const hummus = function(factor)
{
    const ingredient = function(amount, unit, name)
    {
      let ingredientAmount = amount * factor;
      if (ingredientAmount > 1)
      {
        unit += "s";
      }
      console.log(`${ingredientAmount} ${unit} ${name}`);
    };
    ingredient(1, "can", "chickpeas");
    ingredient(0.25, "cup", "tahini");
    ingredient(0.25, "cup", "lemon juice");
    ingredient(1, "clove", "garlic");
    ingredient(2, "tablespoon", "olive oil");
    ingredient(0.5, "teaspoon", "cumin");
};
// tests
for (let i = 2; i < 10; i++)
{
  msgIntro = 'For ' + i + ' people, you need:';
  console.log(msgIntro);
  const dash = function(dashType)
  {
    msgOutro = '';
    for (let j = 0; j < msgIntro.length; j++)
    {
      msgOutro += dashType;
    }
    console.log(msgOutro);
  };
  dash('-');
  hummus(i);
  dash('=');
  console.log('\n');
}
