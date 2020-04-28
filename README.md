oaktree is a python container who mimics xml (this version is a rewrite)

The main element (a Leaf object) can contains two kinds of subs :
- another Leaf
- a string




pas de paramètre de profondeur. Celà rendrait les copier-coller de branches absolument ingérables
la profondeur sera calculée à la volée si c'est vraiment nécessaire.

a été laissé de côté, il faudra apporter la correction dans dump : space n'est valable que sur le Node actuel, alors qu'il devrait être hérité

les fonctions Node.grow() et Node.__init__() peuvent être appelées sans argument. Dans ce cas, l'objet est créé, vide.
