
# Sommaire 

1.  [Introduction](#orgba592fb)
2.  [Ajouter du JavaScript dans un document HTML](#orgbe42000)
3.  [Travailler avec un fichier JavaScript séparé](#org82ccf6b)
4.  [Conclusion](#org9e1fbee)
5.  [Note du traducteur](#org63035fc)



<a id="orgba592fb"></a>

# Introduction

JavaScript, aussi abrégé en JS, est un langage de programmation
utilisé dans le développement web. En tant que technologie de base
du web aux côtés du HTML et du CSS, JavaScript est utilisé pour rendre les
pages interactives et bâtir des applications web. Les navigateurs
web modernes, qui respectent les normes d'affichage communes,
prennent en charge JavaScript via des moteurs intégrés sans
nécessiter de  greffons (*plugins*) supplémentaires.

Lorsqu'il travaille avec des fichiers pour le web, JavaScript doit
être chargé et exécuté aux côtés du HTML. Cela peut être fait soit
en ligne (*inline*) dans un document HTML ou dans un fichier séparé
que le navigateur téléchargera aux du document HTML.

Ce didacticiel couvrera comment incorporer JavaScript dans vos
fichiers web, à la fois en ligne dans un document HTML et comme un
fichier séparé.


<a id="orgbe42000"></a>

# Ajouter du JavaScript dans un document HTML

Vous pouvez ajouter du code JavaScript dans un document HTML en
utilisant la balise dédiée `<script>` qui entoure du code
JavaScript.

La balise `<script>` peut être placée dans la section `<head>` de
votre HTML, dans la section `<body>`, ou après la balise fermante
`</body>`, selon le moment où vous voulez que le JavaScript soit
chargé. 

Généralement, le code JavaScript peut aller à l'intérieur de la
section `<head>` du docuement afin de le garder contenu et hors du
contenu principal de votre document HTML.

Cependant, si votre script a besoin d'être exécuté à un moment
précis avec un affichage de page &#x2013; comme lors de l'usage de
`document.write` pour générer du contenu &#x2013; vous devrez le mettre à
l'endroit où il devrait être appelé, usuellement dans la section
`<body>`. 

Considérons le document HTML vierge suivant avec un navigateur titré
`Today's Date` :

![img](./index.png)

Pour le moment, ce fichier ne contient que du balisage HTML. Disons
que nous aimerions ajouter le code JavaScript suivant au document : 

    let d = new Date();
    alert("Today's date is " + d);

Cela permettra à la page Web d'afficher une alerte avec la date du
jour, quel que soit le moment où l'utilisateur charge le site.

Afin d'accomplir ça, nous ajouterons une balise `<script>` avec du
code JavaScript dans le fichier HTML.

Pour commencer, nous allons ajouter le code JavaScript entre les
balises `<head>`, signalant au navigateur d'exécuter le script
JavaScript avant le chargement dans le reste de la page. Nous
pouvons ajouter le JavaScript sous les balises =<title>, par
exemple, comme indiqué ci-dessous : 

![img](./index2.png)

Une fois la page chargée, vous recevrez une alerte qui ressemblera à
ceci : 

![img](./alert.png)

Vous pouvez également essayer de placer le script à l'intérieur ou à
l'extérieur des balises `<body>` et recharger la page. Comme il ne
s'agit pas d'un document HTML robuste, vous ne remarquerez
probablement aucune différence dans le chargement de la page.

Si nous modifions ce qui est affiché dans le corps du code HTML,
nous aurions besoin de l'implémenter après la section `<head>` pour
qu'il s'affiche sur la page, comme dans l'exemple ci-dessous : 

![img](./index3.png)

La sortie du document HTML ci-dessus chargé via un navigateur Web
ressemblerait à ce qui suit : 

![img](./date.png)

Les scripts qui sont petits ou qui ne fonctionnent que sur une seule
page peuvent fonctionner correctement dans un fichier HTML, mais
pour les scripts plus volumineux ou qui seront utilisés sur
plusieurs pages, ce n'est pas une solution très efficace car
l'inclure peut devenir difficile à lire ou à lire et à
comprendre. Dans la section suivante, nous verrons comment gérer un
fichier JavaScript séparé dans votre document HTML.


<a id="org82ccf6b"></a>

# Travailler avec un fichier JavaScript séparé

Afin de prendre en charge des scripts plus volumineux ou des scripts
utilisés sur plusieurs pages, le code JavaScript réside généralement
dans un ou plusieurs fichiers `js` référencés dans des documents
HTML, de la même manière que les ressources externes telles que CSS.

L'utilisation d'un fichier JavaScript distinct présente les
avantages suivants : 

-   Séparer le balisage HTML et le code JavaScript pour les rendre
    plus simples
-   La séparation des fichiers facilite la maintenance
-   Lorsque les fichiers JavaScript sont mis en cache, les pages se
    chargent plus rapidement

Pour montrer comment connecter un document JavaScript à un document
HTML, créons un petit projet Web. Il se composera de `script.js`
dans le répertoire `js/`, `style.css` dans le répertoire `css/`, et
d'un `index.html` principal à la racine du projet.

![img](./tree.png)

Nous pouvons commencer avec notre modèle HTML précédent de la
section ci-dessus : 

![img](./index4.png)

Passons maintenant à notre code JavaScript qui affichera la date
sous la forme d'un en-tête `<h1>` dans le fichier `script.js` :

![img](./script.png)

Nous pouvons ajouter une référence à ce script dans ou sous la
section `<body>`, avec la ligne de code suivante : 

    <script src="js/script.js"></script>

La balise `<script>` pointe vers le fichier `script.js` du
répertoire `js/` de notre projet Web.

Examinons cette ligne dans le contexte de notre fichier HTML, dans
ce cas, sous la section `<body>` : 

![img](./index4.png)

Enfin, éditons également le fichier `style.css` en ajoutant une
couleur et un style d'arrière-plan à l'en-tête `<h1>` : 

![img](./style.png)

Nous pouvons référencer ce fichier CSS dans la section `<head>` de
notre document HTML : 

![img](./index5.png)

Maintenant, avec JavaScript et CSS en place, nous pouvons charger la
page `index.html` dans le navigateur Web de votre choix. Nous
devrions voir une page qui ressemble à la suivante : 

![img](./blue.png)

Maintenant que nous avons placé le code JavaScript dans un fichier,
nous pouvons l'appeler de la même manière à partir de pages Web
supplémentaires et les mettre à jour tous à un emplacement unique.


<a id="org9e1fbee"></a>

# Conclusion

Ce didacticiel explique comment incorporer JavaScript dans vos
fichiers Web, à la fois en ligne dans un document HTML et dans un
fichier `.js` séparé.

À partir de là, vous pouvez consulter les articles [How To Use The
JavaScript Developer Console](https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-developer-console) et [How to Write Comments in JavaScript](https://www.digitalocean.com/community/tutorials/how-to-write-comments-in-javascript).


<a id="org63035fc"></a>

# Note du traducteur

Ceci est une traduction de l'article [How To Add JavaScript to HTML](https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html)
rédigé par [Lisa Tagliaferri](https://www.digitalocean.com/community/users/ltagliaferri) pour le site [DigitalOcean](https://digitalocean.com/).

# Table des matières

1.  [Introduction](#orgba592fb)
2.  [Ajouter du JavaScript dans un document HTML](#orgbe42000)
3.  [Travailler avec un fichier JavaScript séparé](#org82ccf6b)
4.  [Conclusion](#org9e1fbee)
5.  [Note du traducteur](#org63035fc)
