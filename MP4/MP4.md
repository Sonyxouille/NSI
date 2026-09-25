Projet : annuaire

I] Description du projet

En utilisant les connaissances acquises jusqu'à présent, vous allez écrire un programme écrit en python de gestion de répertoire téléphonique qui doit :

Réaliser une base de données nommée annuaire avec les attributs suivants : Nom, Prénom, N°téléphone, email, qualité.

Gérer cette base de données, c'est- à-dire réaliser l'insertion d'un enregistrement dans la base de données, la suppression d'un enregistrement, la modification d'un enregistrement et la recherche selon au moins 2 critères.

II] Cahier des charges

Réaliser l'une des deux interfaces.

1) Interface minimale

Au lancement du script, le programme proposera le choix suivant dans la console :

1- Ajouter un ou plusieurs enregistrements 

2- Rechercher dans le répertoire 

3- Modification d'un enregistrement

4- Suppression d'un enregistrement

5- Quitter

Quel est votre choix ?

Tant que le choix saisi n'aura pas la valeur 1,2, 3, 4 ou 5, le logiciel vous redemandera votre choix. Il quittera lorsque le choix n°5 uniquement sera fait.

Pour le choix n°1, Le logiciel vous demande le nombre d'enregistrements. Puis après avoir saisi votre réponse, le logiciel affiche :

ajout n°1 expression régulière: 

nom, prenom, numéro de téléphone (commence par 0), email, qualité

(peut être vide mettre 1 espace après la virgule):


Pour le choix n°2, le logiciel demandera un critère de choix pour la recherche et l'effectuera. Si le logiciel trouve l'enregistrement, il l'affichera. Si il ne le trouve pas, il affiche enregistrement inconnu.

Pour le choix n°3, le logiciel demandera un critère de choix pour la modification puis modifiera l'enregistrement

Pour le choix n°4, le logiciel demandera un attribut puis effacera l'enregistrement.

Si le choix n°5 est fait, le programme quitte.

2) Interface complexe

Réaliser avec Tkinter une interface graphique à l'instar de la réalisation expliquée sur le (site)[https://nsi.xyz/projets/systeme-de-gestion-de-base-de-donnees-relationnelle-sur-les-jeux-videos-en-python/]. Cette interface devra proposer les mêmes possibilités que l'interface minimale.