# projet_maths_info


\section{Le Clustering}


Le clustering est une méthode d'analyse statistique utilisée pour organiser des données brutes en silos homogènes.  A l'intérieur de chaque grappe, les données sont regroupées selon une caractéristique commune.L'outil d' ordonnancement est un algorithme qui mesure la proximité entre chaque élément à partir de critères définis.

Avant que l’intelligence artificielle des ordinateurs ne devienne capable de détecter des similarités entre individus, ce sont bien des intelligences humaines qui ont implémenté les algorithmes de clustering.

Il en existe plusieurs dizaines, dont voici plusieurs grandes catégories.
Pour chaque méthode, il est nécessaire de choisir comment mesurer la similarité entre deux individus – qu’on peut imaginer comme deux points de l’espace des réels en dimension p.

Il nous faut donc une fonction distance, comme par exemple la distance euclidienne. Les n individus sont des « points » de l’espace de variables R en dimension p.


\section{méthodes de clustering}

$$$2.1 Les méthodes hiérarchiques$$$

Les méthodes de clustering de type hiérarchique sont différentes. Elles forment pas à pas des connexions entre individus (pour les méthodes de clustering hiérarchiques ascendantes), et utilisent une matrice de distances entre individus pour trouver le regroupement le plus proche d’un autre.

En pratique, on part de n ensembles qui sont les individus en tant que singletons. La première connexion se fait donc entre les deux individus les plus proches.

Pour débuter la deuxième étape, il faut mettre à jour la matrice des distances en enlevant une case, à cause du regroupement de deux individus. Mais comment calculer la distance d’un ensemble à un autre s’il n’est pas un singleton ? C’est justement un des choix à effectuer au départ : la stratégie d’agrégation. Il y en a de multiples, les plus simples étant de choisir la distance minimale entre les individus des deux groupes (single linkage), maximale (complete linkage) ou bien moyenne (average linkage).

A la fin de cette deuxième étape, on connecte donc les deux groupes les plus proches. Et ainsi de suite pour les étapes suivantes, jusqu’à connecter les deux derniers groupes qui recouvrent tous les individus.

Les connexions successives se représentent sur un dendrogramme (cf illustration). La distance associée à chaque connexion se trouve sur l’axe y de celui-ci.

L’algorithme se termine bien sûr par le choix de nos clusters. Là encore, le critère n’est pas unique : on peut en vouloir un nombre précis, ou bien fixer un critère de distance inter-classe. On utilise le dendrogramme pour mettre les clusters en évidence.



$$$ 2.2 Les méthodes centroïdes$$$

La méthode centroïde la plus classique est la méthode des k-moyennes. Elle ne nécessite qu’un seul choix de départ : k, le nombre de classes voulues.
On initialise l’algorithme avec k points au hasard parmi les n individus.

Ces k points représentent alors les k classes dans cette première étape. On associe ensuite chacun des n-k points restants à la « classe-point » qui lui est la plus proche. A la fin de cette première étape, chaque classe est caractérisée par la moyenne des valeurs de chacun de ses individus. On a k moyennes pour k classes.

La deuxième étape consiste à évaluer la distance de chaque individu à chacune des k moyennes. Certains individus peuvent ici changer de classe. A la fin de cette étape, on actualise les k moyennes. Et on réitère les étapes, jusqu’à ce qu’il y ait convergence pour obtenir nos k clusters finaux.

Ces classes finales dépendent souvent beaucoup des k individus choisis pour l’initialisation. C’est pourquoi certains algorithmes de k-means itèrent plusieurs fois le processus avec des initialisations différentes, dans le but de garder la partition qui minimise le plus la variance intra-classe (somme des distances entre les individus d’une même classe).

On prend l'exemple de l'algorithme de K-maens (voir code )

$$$interpretation$$$ 

Les points noirs sont les centres des classes, actualisés à chaque étape. On observe bien le phénomène de convergence de ces n centres mobiles
