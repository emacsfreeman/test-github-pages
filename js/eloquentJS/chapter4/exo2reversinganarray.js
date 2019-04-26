function reverseArray(tab)
{
    let result = [];
    for (let i = 0; i < tab.length; i++)
    {
        result.push(tab[tab.length - 1 - i]);
    }
    return result;
}

// Test
chiffres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
inverseChiffres = reverseArray(chiffres);

function afficheTableau(tab, ordre)
{
  let phrase = "Tableau des chiffres dans l'ordre " + ordre + " :";
  console.log(phrase);
  console.log("-".repeat(phrase.length));
    
  if (ordre.toUpperCase() === "CROISSANT") console.log(tab);    
  else if (ordre.toUpperCase() === "décroissant".toUpperCase())   console.log(reverseArray(tab));
  else console.log('Error!');
}

afficheTableau(chiffres, "croissant");
console.log("\n\n");
afficheTableau(chiffres, "décroissant");


function reverseArrayInPlace(tab)
{
	let temp = 0;
	for (let i = 0; i < tab.length / 2; i++)
	{
		temp = tab[i];
		tab[i] = tab[tab.length - i - 1];
		tab[tab.length - i - 1] = temp
	}
	return tab;
}

// Test
function afficheTableau(tab, ordre)
{
  let phrase = "Tableau des chiffres dans l'ordre " + ordre + " :";
  console.log(phrase);
  console.log("-".repeat(phrase.length));
    
  if (ordre.toUpperCase() === "CROISSANT") console.log(tab);    
  else if (ordre.toUpperCase() === "décroissant".toUpperCase())   console.log(reverseArrayInPlace(tab));
  else console.log('Error!');
}

chiffres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
afficheTableau(chiffres, "croissant");
console.log("\n");
afficheTableau(chiffres, "décroissant");

console.log(chiffres === reverseArrayInPlace(chiffres));

// Book's solutions
function reverseArray(array) {
  let output = [];
  for (let i = array.length - 1; i >= 0; i--) {
    output.push(array[i]);
  }
  return output;
}

function reverseArrayInPlace(array) {
  for (let i = 0; i < Math.floor(array.length / 2); i++) {
    let old = array[i];
    array[i] = array[array.length - 1 - i];
    array[array.length - 1 - i] = old;
  }
  return array;
}
