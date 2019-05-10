// Exo1: Flattening

let digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
for (digit in digits)
    console.log(digit);

let vowels = ['a', 'e', 'i', 'o', 'u'];
for (vowel in vowels)
    console.log(vowel);

let someFiatCurrencies = ['€', '$', '£'];
for (fiat in someFiatCurrencies)
    console.log(fiat);

let someCryptoCurrencies = ['BTC', 'ETH', 'LTC'];
for (crypto in someCryptoCurrencies)
    console.log(crypto);

let arrayToFlatten = [
    digits,
    vowels,
    someFiatCurrencies,
    someCryptoCurrencies
];
for (array in arrayToFlatten)
    console.log(array);

console.log(arrayToFlatten.reduce((flat, current) => flat.concat(current), []));


// Exo2: Your own loop
function loop(start, test, update, body)
{
    for (let value = start; test(value); value = update(value))
    {
	body(value);
    }
}

loop(3, n => n > 0, n => n - 1, console.log);
// → 3
// → 2
// → 1

// Exo3: Everything
function every(array, predicate)
{
    for (let element of array)
    {
	if (!predicate(element)) return false;
    }
    return true;
}

function every2(array, predicate)
{
  return !array.some(element => !predicate(element));
}

console.log(every([1, 3, 5], n => n < 10));
// → true
console.log(every([2, 4, 16], n => n < 10));
// → false
console.log(every([], n => n < 10));
// → true

// Exo4: Dominant writing direction
function dominantDirection(text)
{
  let counted = countBy(text, char => {
    let script = characterScript(char.codePointAt(0));
    return script ? script.direction : "none";
  }).filter(({name}) => name != "none");

  if (counted.length == 0) return "ltr";

  return counted.reduce((a, b) => a.count > b.count ? a : b).name;
}

console.log(dominantDirection("Hello!"));
// → ltr
console.log(dominantDirection("Hey, مساء الخير"));
// → rtl
