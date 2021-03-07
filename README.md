# projet_maths_info


\section{Le Clustering}


Le clustering est une méthode d'analyse statistique utilisée pour organiser des données brutes en silos homogènes.  A l'intérieur de chaque grappe, les données sont regroupées selon une caractéristique commune.L'outil d' ordonnancement est un algorithme qui mesure la proximité entre chaque élément à partir de critères définis.

Avant que l’intelligence artificielle des ordinateurs ne devienne capable de détecter des similarités entre individus, ce sont bien des intelligences humaines qui ont implémenté les algorithmes de clustering.

Il en existe plusieurs dizaines, dont voici plusieurs grandes catégories.
Pour chaque méthode, il est nécessaire de choisir comment mesurer la similarité entre deux individus – qu’on peut imaginer comme deux points de l’espace des réels en dimension p.

Il nous faut donc une fonction distance, comme par exemple la distance euclidienne. Les n individus sont des « points » de l’espace de variables R en dimension p.

\section{L’importance du clustering dans la science des données}
La but des algorithmes de clustering est de donner un sens aux données et d’extraire de la valeur à partir de grandes quantités de données structurées et non structurées. Ces algorithmes nous permettent de séparer les données en fonction de leurs propriétés ou fonctionnalités et de les regrouper dans différents clusters en fonction de leurs similitudes.

Les algorithmes de clustering ont plusieurs utilisations dans différents secteurs. Par exemple, nous avons besoin d’algorithmes de classification pour classer les maladies en science médicale. Parallèlement, le clustering nous aide à classer les clients dans le domaine des études de marché.

\section{Les différentes implémentations}
Il existe plusieurs manières d’implémenter ce partitionnement, en fonction de modèles distincts. Des algorithmes propres sont appliqués à chaque modèle, en différenciant ses propriétés et ses résultats. Ces modèles se distinguent par leur organisation et leur type de relation. Les plus importants sont:

Groupe: les algorithmes ont uniquement des informations de cluster

Centralisé : chaque cluster est représenté par une seule moyenne vectorielle et une valeur d’objet est comparée à ces valeurs moyennes.

Graphique: l’organisation en grappe et la relation entre les membres sont définies par une structure de graphe

Densité: les membres du groupe sont regroupés par régions où les observations sont denses et similaires.

Distribué: le cluster est construit à l’aide de distributions statistiques

Connectivité: La connectivité de ces modèles est basée sur une fonction de distance entre éléments.


\section{méthodes de clustering}

$$$\item{ 4.1 Les méthodes hiérarchiques}$$$$

Les méthodes de clustering de type hiérarchique sont différentes. Elles forment pas à pas des connexions entre individus (pour les méthodes de clustering hiérarchiques ascendantes), et utilisent une matrice de distances entre individus pour trouver le regroupement le plus proche d’un autre.

En pratique, on part de n ensembles qui sont les individus en tant que singletons. La première connexion se fait donc entre les deux individus les plus proches.

Pour débuter la deuxième étape, il faut mettre à jour la matrice des distances en enlevant une case, à cause du regroupement de deux individus. Mais comment calculer la distance d’un ensemble à un autre s’il n’est pas un singleton ? C’est justement un des choix à effectuer au départ : la stratégie d’agrégation. Il y en a de multiples, les plus simples étant de choisir la distance minimale entre les individus des deux groupes (single linkage), maximale (complete linkage) ou bien moyenne (average linkage).

A la fin de cette deuxième étape, on connecte donc les deux groupes les plus proches. Et ainsi de suite pour les étapes suivantes, jusqu’à connecter les deux derniers groupes qui recouvrent tous les individus.

Les connexions successives se représentent sur un dendrogramme (cf illustration). La distance associée à chaque connexion se trouve sur l’axe y de celui-ci.

L’algorithme se termine bien sûr par le choix de nos clusters. Là encore, le critère n’est pas unique : on peut en vouloir un nombre précis, ou bien fixer un critère de distance inter-classe. On utilise le dendrogramme pour mettre les clusters en évidence.



$$$\item{ 4.2 Les méthodes centroïdes}$$$

La méthode centroïde la plus classique est la méthode des k-moyennes. Elle ne nécessite qu’un seul choix de départ : k, le nombre de classes voulues.
On initialise l’algorithme avec k points au hasard parmi les n individus.

Ces k points représentent alors les k classes dans cette première étape. On associe ensuite chacun des n-k points restants à la « classe-point » qui lui est la plus proche. A la fin de cette première étape, chaque classe est caractérisée par la moyenne des valeurs de chacun de ses individus. On a k moyennes pour k classes.

La deuxième étape consiste à évaluer la distance de chaque individu à chacune des k moyennes. Certains individus peuvent ici changer de classe. A la fin de cette étape, on actualise les k moyennes. Et on réitère les étapes, jusqu’à ce qu’il y ait convergence pour obtenir nos k clusters finaux.

Ces classes finales dépendent souvent beaucoup des k individus choisis pour l’initialisation. C’est pourquoi certains algorithmes de k-means itèrent plusieurs fois le processus avec des initialisations différentes, dans le but de garder la partition qui minimise le plus la variance intra-classe (somme des distances entre les individus d’une même classe).

On prend l'exemple de l'algorithme de K-maens (voir code )

$$$interpretation$$$ 

Les points noirs sont les centres des classes, actualisés à chaque étape. On observe bien le phénomène de convergence de ces n centres mobiles

$$$4.3 Modèles de distribution$$$

ces modèles de clustering sont basés sur la notion de la probabilité que tous les points de données du cluster appartiennent à la même distribution (par exemple: normale, gaussienne). Ces modèles souffrent souvent de surajustement. Un exemple populaire de ces modèles est l'algorithme de maximisation des attentes qui utilise des distributions normales multivariées.

$$$4.4 Modèles de densité$$$

ces modèles recherchent dans l'espace de données des zones de densité variée de points de données dans l'espace de données. Il isole diverses régions de densité différentes et attribue les points de données au sein de ces régions dans le même cluster. DBSCAN et OPTICS sont des exemples populaires de modèles de densité.


\section{regression clustering}
l'algorithme est assez simple à décrire. Le nombre de clusters, K, pour une exécution donnée est fixe. Les lignes sont triées aléatoirement dans les groupes pour former K grappes initiales. Un algorithme d'échange est appliqué à cette configuration initiale qui recherche les lignes de données qui produiraient une diminution maximale d'une fonction de pénalité des moindres carrés (c'est-à-dire maximiser l'augmentation de R-carré à chaque étape). L'algorithme continue jusqu'à ce qu'aucun échange utile de lignes ne puisse être trouvé.

\section{Les types des méthodes de Classifications }
On peut grouper les méthodes classificatoires en deux grandes familles , cette fois-ci , on
prends en considération l’intervention ou non d’un « attribut classe » au fur et à mesure
du processus de la classification, ces deux types sont : « supervisée (Classement)» et « non
supervisée(Classification, Clustering) »,

1. supervisé (classement) : groupes fixés, exemples d’objets de chaque groupe.


2. non supervisé (classification) : on ne connaît pas de groupe.
Cependant, Il existe d’autres types de classification qui s’appuient sur d’autres types de
méthodes d’apprentissages comme « l’apprentissage semi-supervisé » et « l’apprentissage par
renforcement ». En effet, l’apprentissage semi-supervisé est un bon compromis entre les deux
types d’apprentissage « supervisé » et « non-supervisé », car il permet de traiter un grand
nombre de données sans avoir besoin de toutes les étiqueter, et il profite des avantages des
deux types mentionnés. Alors que L’apprentissage par renforcement est fort utilisé dans le cas
d’apprentissage interactif
