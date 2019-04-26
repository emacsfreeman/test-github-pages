function countBs(chaine)
{
    let compteur = 0;
    for (let i = 0; i < chaine.length; i++)
    {
        if (chaine[i] === "B") compteur++;
    }
    return compteur;
}

// Test
chaine = "Bonjour Bernard Brun, ça va bien ?";
console.log("Il y a " + countBs(chaine) + " 'B' dans la phrase : \n<< " + chaine + " >>");

function countChar(chaine, caractere)
{
    let compteur = 0;
    for (let i = 0; i < chaine.length; i++)
    {
        if (chaine[i] === caractere) compteur++;
    }
    return compteur;
}

// Test
chaine = "Bonjour Bernard Brun, ça va bien ?";
caractere = 'n';
console.log("Il y a " + countChar(chaine, caractere) + " '" + caractere + "' " + "dans la phrase : \n<< " + chaine + " >>");
