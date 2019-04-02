// console.log('Hello World');

const fs = require('fs');
fs.writeFileSync('notes.txt', 'This file was created by Node.js\n');






// Défi
// Ajouter un message à notes.txt
//
// 1. Utiliser appendFileSync
// 2. Exécuter le script
// 3. Vérifier en ouvrant le fichier

// fs.appendFileSync('message.txt', 'data to append\n');


// Solution 1
// fs.appendFileSync('notes.txt', 'Nouveau message ajouté\n');

// Solution 2
fd = fs.openSync('notes.txt', 'a');
fs.appendFileSync(fd, 'Message ajouté\n', 'utf8');
