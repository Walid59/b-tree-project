#### projet L3S6 sur les arbres B réalisé par ROUABAH Walid & Mohamed-Amine Fathallah

### Ce qui a été réalisé:
1) Insertion
2) Recherche
3) Documentation

### Ce qui n'a pas été réalisé ou réalisé partiellement:
La suppression

## Sommaire :  
I) Fonctionnement du code et de la documentation
1) Comment créer un arbre
2) Comment ajouter une valeur
3) Comment chercher une valeur  

II) Explication du code et exemples sur la recherche et l'insertion
1) Pour la recherche
2) Pour l'insertion

## I) Fonctionnement du code
Il est expliqué ici comment créer un arbre, puis lui insérer des valeurs et comment rechercher les valeurs.

1) ###  Comment créer un arbre :
Pour créer un arbre, il suffit de créer un objet de la classe Tree qui possède 2 paramètres obligatoires : 
- le nombre de fils minimal + 1 (L)
  - le nombre de fils maximal + 1 (U)

Par exemple, pour créer un arbre avec un fils minimal et 2 fils maximal on fera alors:  
`tree = Tree(2,3)`

2) ###  Comment ajouter une valeur :
On suppose ici qu'on a arbre nommé _tree_ qui existe déjà pour les exemples.
- Pour ajouter un seul élément à un arbre, il suffit de faire :  `tree.insert(key)`  
où key correspond à un nombre entier quelconque.


- Pour ajouter plusieurs valeurs à la fois, il suffit de faire :`tree.insert(l)`  
où l correspond à une liste quelconque contenant 0 ou plusieurs entiers.

3) ###  Pour chercher une valeur :
C'est tout simple, il suffit de taper : `tree.exists_key(key)`  
où key correspond correspond à la clé qu'on veut chercher dans l'arbre.

4) ### Fonctionnement et génération de la documentation 
La documentation sous format HTML a été générée grâce à Sphinx. 
Les fichiers html de la documentation sont contenus dans docs/_build/html.

**[OPTIONNEL]**  
Je me permets de donner les commandes même si la documentation a déjà été générée :  
1) _mkdir docs_ -> à la racine du projet, j'ai crée un dossier docs qui gère toute la documentation du projet.  
2) _cd docs_  -> car maintenant pour gérer la documentation tout se fait la dedans
3) _sphinx-quickstart_ -> pour initialiser sphinx dans le dossier docs
4) Quelques modifications au niveau du fichier docs/conf.py où j'ai décommenté la ligne 13 à 15,
et où j'ai ajouté une extension à la ligne 31 pour faire fonctionner la génération de l'HTML.
5) ajouté à la ligne 13 le mot *modules* du fichier docs/index.rst pour que tous les fichiers pythons du projets soient comptabilisés dans la doc HTML.
6) sphinx-apidoc.exe -o . .. -> commande qui a généré le fichier html dans docs/_build/html  


## II) Explication du code et exemples sur la recherche et l'insertion
On parlera ici de manière détaillée de toutes les situations différentes auquels on peut tomber quand on recherche une clé ou quand on ajouter une clé dans l'arbre,
en citant et en expliquant le code, avec des illustrations issues du site https://www.cs.usfca.edu/~galles/visualization/BTree.html.

1) ###  La recherche
Voir mail du prof (10 fevrier) sur la doc et le lien qu'il a envoyé : https://gitlab-ens.fil.univ-lille1.fr/lepallec/l3s6-projet/-/blob/main/documentation.md

2) ###  L'insertion