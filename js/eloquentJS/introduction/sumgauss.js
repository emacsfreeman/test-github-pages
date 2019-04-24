// petit script qui compte la somme des entiers de 1 à 10 : 1 + 2 + ... + 10 = 55
let total = 0, count = 1;
while (count <= 10) 
{
  total += count;
  count += 1;
}
console.log(total); // affiche 55
