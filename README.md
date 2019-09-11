Aujourd’hui, la robotique prend de plus en plus de place et nous aide à accomplir les tâches quotidiennes. Cette science évolue rapidement au point de produire des robots très intelligents, capables d’apprendre d’eux-mêmes. Ils ne sont plus appelés des robots simples, mais plutôt des intelligences artificielles.
                    Eva, l’une d’entre-elles, est une intelligence artificielle conçue pour aider nos enfants à apprendre la grammaire. Le concepteur d’Eva a implémenté un algorithme capable d’apprendre plusieurs règles pour écrire et lire correctement. Mais lors de la phase des tests, on a remarqué qu’Eva ne savait pas distinguer une phrase qui ne contient pas d’erreurs de  parenthèse d’une autre qui n’en contient pas. Idem pour les crochets.
TACHE

      Le concepteur se trouve face à un problème, d’autant plus que les délais de livraison de l’intelligence artificielle ont été largement dépassés. Ils implorent votre aide pour aide. Proposez-lui un algorithme qui puisse voir les phrases mal orthographiée dans un texte, mais aussi voudrait que vous puissiez y ajouter d’autres requêtes comme le montre l’exemple suivant.
DESCRIPTION DU PROBLEME

Voici un texte contenant ces différentes erreurs, suivez l’exemple pour proposer une solution.
InputFile text.
Lorem ipsum dolor sit amet, (consectetur) adipiscing elit. Nunc) fringilla metus eget) elit tristique (dignissim. Mauris id nisi (et tortor fringilla tincidunt) sed sit amet elit. Aliquam feugiat velit sollicitudin, tempor velit et, maximus sem. Etiam (varius tincidunt est. Proin (mattis convallis) tincidunt phasellus euismod tortor eget vestibulum sollicitudin, mi lorem eleifend libero, non consequat sem velit in elit. Ut nisi felis, lacinia nec elit non, lacinia rutrum urna. Quisque (vitae sagittis) diam, ut lobortis nisi. Maecenas id massa velit phasellus et massa laoreet, maximus diam aliquam, ) accumsan elit. 
Le fichier de solution aura le format suivant.
Output file	

9	
Le nombre de phrases qui composent le texte.


3	
Les phrases mal-orthographiées.
Lorem ipsum dolor sit amet, (consectetur) adipiscing elit. Nunc !error fringilla metus eget !error elit tristique !error dignissim. Mauris id nisi (et tortor !error fringilla tincidun) sed sit amet elit. Aliquam feugiat velit sollicitudin, [tempor velit] et, maximus sem. Etiam !error varius tincidun t!error est. Proin (mattis convallis) tincidunt !error phasellus euismod tortor eget vestibulum sollicitudin, mi lorem eleifend libero, non consequat sem velit in elit. Ut nisi felis, lacinia nec elit non, lacinia rutrum urna. Quisque (vitae sagittis) diam, ut lobortis nisi. Maecenas [id massa] velit phasellus et massa laoreet, maximus diam aliquam, !error accumsan elit.	Mettre le nouveau texte en remplaçant les signes mal-placés par le mot-clé !error.
                     

Voici alors un nouveau texte, concevez et implémenter votre solution afin de faire évoluer Eva. Vous aurez fait progresser la science ainsi donc l’humanité.

NOTATION
La note maximale est de cent points (100).La notation se base sur plusieurs critères notamment sur une solution plus simples et moins couteuse en ressources. D’abord, présenter un projet qui puisse être lancé sur une plateforme sans erreur de débogage sera sanctionné automatiquement de 25 points. Trouver le nombre exact de phrases qui composent le texte est sur cinq points. Chaque parenthèse ouvrante ou fermante mal placée constitue une erreur à détecter et à résoudre. Une erreur corrigée vous donne un point.

NB : Le jury se réserve le droit d’ajouter dix points à du code bien clair et commenté. Veuillez bien expliciter toutes vos fonctionnalités dans les commentaires ou bien le nom propre de chaque fonction. 
MERCI !
