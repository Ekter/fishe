# setup service

Il faut tout d'abord déplacer les fichiers `dump-database.service` et `dump-database.timer` dans `/etc/systemd/system/`.

Ensuite, il faut relancer le daemon systemd pour prendre en compte les nouveaux fichiers.

```bash
sudo systemctl daemon-reload
```

Enfin, il faut activer et lancer le timer pour que le service se lance toutes les 10 minutes.

```bash
sudo systemctl enable dump-database.timer
sudo systemctl start dump-database.timer
```
