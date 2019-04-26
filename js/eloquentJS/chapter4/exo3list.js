function arrayToList(tab)
{
  let list = null;
  for (let i = tab.length - 1; i >= 0; i--)
  {
    list = {value: tab[i], rest: list};
  } 
  return list;
}

// Test
let liste = arrayToList([1, 2, 3]);
console.log(liste)
console.log(liste.value);
console.log(liste.rest.value);
console.log(liste.rest.rest.value);

function prepend(value, list) 
{
  return {value, rest: list};
}

// Test
let value = 4;
console.log("\nLa liste de départ : ");
console.log(liste)
console.log("\nLa liste après ajout de la valeur en 1ère position : ");
let listeAugmentee = prepend(value, liste);
console.log(listeAugmentee);


function nth(list, n) 
{
  if (!list) return undefined;
  else if (n == 0) return list.value;
  else return nth(list.rest, n - 1);
}

// Test
let listF = listeAugmentee;
for(let n = 0; n < 4; n++)
{
  console.log("\nValeur en position " + n + " de la liste " + listF + " : " + nth(listF, n));
}
