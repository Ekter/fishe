# setup logrotate

```sh
logfile {
size 10k
daily
rotate 7
compress
missingok
}
```

je limite la taille des fichiers à 10 000 octets parce que normalement si il y a une erreur, elle est la même tout le temps, donc je ne veux pas garder des fichiers de 100 Mo.
j'archive tous les jours et je rotate toutes les semaines, en gardant les fichiers compressés pour gagner de la place.
