//
// Défi : définir et utiliser une fonction
// dans un fichier
//
// 1. Créer un nouveau fichier notes.js
// 2. Créer une fonction getNotes qui
//     renvoie "Your notes..."
// 3. Exporter la fonction getNotes
// 4. Depuis app.js, charger et appeler
//    la fonction en affichant un message dans
//    la console


const add = require('./utils.js');
//const firstName = require('./utils.js');

//const name = "Laurent";

// console.log(firstName);

const sum = add(4, -2);
console.log(sum);
