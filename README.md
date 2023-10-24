# lightManager
Light Manager Module

[Light Effect List](https://www.pc-100.com/mechanical-keyboard-features-parameters/back-light-effects-mechanical-keyboard/)

Fonctionnalité bientôt disponible :
- Séquence personnalisée de lumière (modularité)
- Niveau de batterie (trouver une bonne fonction de conversion voltage -> level)
- Ripple Effect
- Modularité

Fonctionnalité déjà disponible :
- Effet de respiration (rouge, vert, bleu)
- Raimbow wave effect (séquencer) -> Trouver une façon d'automatiser en fonction de la taille
- Réaction de clique

Fonctionnalité à ajouté :
- Initialisation pour taille de cube variable (modularité)
- Connexion avec l'interface permettant de créer des effets
- Heat Map
- Ajout d'un système de temps pour définir la durée d'un effet (utilisation de time impossible -> redemander à Adrien le nom du système)

Conception actuelle :
- Utilisation de 5 tableaux 1D (topFace, northFace, southFace, eastFace, westFace)
- Conception d'effet par séquençage (tableaux de Tableaux)
