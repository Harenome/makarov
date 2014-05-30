Makarov
=======
[![Build Status][]][Travis CI Makarov] [![Coverage Status][]][Coveralls Makarov]

[Coveralls Makarov]: https://coveralls.io/r/Harenome/makarov
[Coverage Status]: https://img.shields.io/coveralls/Harenome/makarov.svg
[Travis CI Makarov]: https://travis-ci.org/Harenome/makarov
[Build Status]: https://travis-ci.org/Harenome/makarov.svg?branch=master

Projet Makarov. Chaînes de Markov.

Récupérer Makarov
-----------------
```bash
$ git clone https://github.com/Harenome/makarov.git
```

Lancer Makarov
--------------
Au choix:
```bash
$ ./makarov.py [--verbose]
$ ./run [--verbose]
```
Chaque utilisateur devra taper son texte, et le valider en appuyant sur
```ENTRÉE```.

Lire l'aide depuis l'interpréteur
---------------------------------
```bash
$ python
```
Puis dans l'interpréteur:
```python
>>> from makarov import *
>>> from makarov.markov_chain import MarkovChain
>>> from makarov.markov_time import MarkovTimeReader
>>> help(getch)
>>> help(markov_chain)
>>> help(markov_time)
>>> help(MarkovChain)
>>> help(MarkovTimeReader)
```

License
-------
Copyright © 2014 MEYER Jérémy, RAZANAJATO RANAIVOARIVONY Harenome, WHILHELM Stan

Ce projet est libre. Vous pouvez le redistribuer ou le modifier selon les termes
de la license « Do What The Fuck You Want To Public License », Version 2, comme
publiée par Sam Hocevar. Pour de plus amples informations, veuillez vous référer
au fichier COPYING, ou bien http://www.wtfpl.net/.
