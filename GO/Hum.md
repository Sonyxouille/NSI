#set document(title: "La récursivité en informatique", author: "Sonyxou")
#set text(font: "Libertinus Serif", size: 10.5pt, lang: "fr")
#set heading(numbering: "1.")
#show heading.where(level: 1): set text(size: 19pt, weight: "bold", fill: rgb("17365D"))
#show heading.where(level: 2): set text(size: 13pt, weight: "bold", fill: rgb("245B83"))
#show link: set text(fill: rgb("1266A0"))

#align(center)[
  #text(size: 11pt, weight: "bold", fill: rgb("52718A"))[TERMINALE — NUMÉRIQUE ET SCIENCES INFORMATIQUES]
  #v(0.25cm)
  #text(size: 27pt, weight: "bold", fill: rgb("17365D"))[La récursivité]
]

#block()[
  #text(size: 20pt, weight: "bold")[Problématique : ]

  #text(size: 13pt, weight: "bold")[Comment la récursivité permet-elle de résoudre des problèmes complexes en informatique, et quelles sont ses limites ?]
]

= Introduction

En informatique, certains problèmes peuvent être résolus en répétant une même opération sur une partie de plus en plus petite du problème initial. C'est le principe de la *récursivité* : une fonction récursive est une fonction qui s'appelle elle-même. Elle demande cependant une condition d'arrêt, les appels peuvent se poursuivre jusqu'à provoquer une erreur.

= Comprendre le principe

== Définition

#quote(block: true)[
  « On dit qu'un sous-programme (procédure ou fonction) est récursif s'il s'appelle lui-même. »
]

Cette définition signifie qu'une fonction récursive déclenche un nouvel appel à elle-même pour traiter une version plus simple du problème initial.

Cela nécessite également une condition d'arrêt :

#quote(block: true)[
  « Il est indispensable de prévoir une condition d'arrêt à la récursion sinon la fonction va s'appeler une infinité de fois. »
]

Une fonction récursive repose donc sur deux éléments essentiels :

- *La condition d'arrêt* : dont on connaît directement la réponse.
- *La boucle récursive* : dans laquelle la fonction s'appelle à nouveau avec un problème plus petit ou plus simple.

Il faut aussi vérifier que les appels successifs se rapprochent de la condition d'arrêt. Sinon la fonction risque de ne jamais terminer.

== Exemple : calculer la somme des entiers

Pour calculer la somme des entiers de 0 à `n`, on peut utiliser la relation :

- si `n == 0`, la somme vaut `0` ;
- sinon, la somme vaut `n + somme(n - 1)`.

#raw("def somme(n: int) -> int:\n    if n == 0:          # condition d'arrêt\n        return 0\n    else:               # boucle récursive\n        return n + somme(n - 1)\n\nprint(somme(3))  # affiche 6\n", block: true, lang: "python")

Pour `somme(3)`, les appels se succèdent ainsi : `somme(3)` attend `somme(2)`, qui attend `somme(1)`, qui attend `somme(0)`. Le cas de base renvoie `0`, puis les résultats remontent : `somme(1) = 1`, `somme(2) = 3` et `somme(3) = 6`.

== Fonctionnement

Chaque fonction s'appelle elle-même avec une version plus petite et plus simple à résoudre. Cela s'appelle un *arbre d'appels*.

Exemple : `somme(3)` attend le résultat de `somme(2)`, qui attend celui de `somme(1)`, jusqu'à `somme(0)`. Une fois ce dernier appel terminé, les résultats sont calculés en remontant : `somme(1) = 1`, puis `somme(2) = 3`, et enfin `somme(3) = 6`.

= À quoi sert la récursivité ?

La récursivité est utilisée pour résoudre des problèmes qui peuvent être décomposés en plusieurs sous-problèmes. Elle est notamment utile dans différentes situations :

- *Rechercher un chemin dans un labyrinthe* : comme le montre la vidéo de Lumni, la récursivité peut servir à explorer les différents chemins possibles jusqu'à trouver une sortie ou constater qu'un chemin ne mène pas au résultat attendu.
- *Utiliser la méthode « diviser pour régner »* : certains algorithmes, comme le tri par fusion, découpent un problème en plusieurs problèmes plus petits, les résolvent séparément, puis réunissent les résultats.

La récursivité est donc particulièrement intéressante lorsque les étapes d'un problème se répètent ou lorsqu'il peut être divisé en problèmes plus simples.

= Les limites et la comparaison avec l'itération

Une solution récursive n'est pas automatiquement plus rapide ou plus efficace qu'une solution écrite avec une boucle (`for` ou `while`). Les deux méthodes peuvent être utilisées pour programmer certains traitements, mais qu'elles n'ont pas les mêmes caractéristiques :

#quote(block: true)[
  « La méthode récursive est plus élégante et lisible [...] L'inconvénient le plus important de cette méthode, est qu'une fois implémentée dans un langage de programmation, elle est très gourmande en ressource mémoire. »
]

Chaque appel supplémentaire utilise de la mémoire pour stocker son contexte. En Python, un trop grand nombre d'appels imbriqués peut dépasser la limite autorisée et provoquer une erreur `RecursionError`. Il faut donc toujours prévoir une condition d'arrêt et s'assurer que chaque appel rapproche de ce cas. Pour un traitement répétitif simple ou très long, une version itérative peut être préférable.

#table(
  columns: (1fr, 1fr),
  inset: 7pt,
  [*Récursivité*], [*Itération*],
  [La fonction s'appelle elle-même.], [Le programme utilise une boucle.],
  [Utilise l'arbre d'appels, donc de la mémoire supplémentaire.], [Évite l'empilement d'appels récursifs.]
)

= Sources et ressources complémentaires

*Ressource de vulgarisation —* #link("https://www.lumni.fr/video/une-introduction-a-la-recursivite")[« Une introduction à la récursivité », Les cours Lumni – Lycée, Numérique et sciences informatiques, 30 min 29, publiée le 16 décembre 2020].

*Vidéo complémentaire —* #link("https://www.youtube.com/watch?v=QMDRNv_O8tU")[« La récursivité en informatique - NSI - Terminale », Stéphane Vercleven, YouTube].

*Cours de la classe —* #link("https://ga78523.github.io/mkdocs_cours/Terminale/Programmation/cours_recursivite/")[Chapitre « Récursivité », site de cours].

= Conclusion

La récursivité est une méthode de programmation qui permet de résoudre un problème en le décomposant en problèmes plus simples. Comme le présente la vidéo de Lumni, elle peut notamment être utilisée pour rechercher un chemin dans un labyrinthe ou mettre en œuvre des algorithmes comme le tri par fusion.

Son utilisation nécessite cependant de prévoir une condition d'arrêt afin de garantir la fin des appels récursifs. De plus, chaque appel utilise de la mémoire, ce qui peut rendre cette méthode moins efficace qu'une solution utilisant l'itérativité. La récursivité est utilisable à condition qu'elle n'engrange pas trop d'appels.