
# Réalisation d’un script de sauvegarde de base de données

Enoncé :

* Installez MySQL sur votre VM
* Créez la base de données à partir du fichier de backup suivant : <https://www.mysqltutorial.org/wp-content/uploads/2018/03/mysqlsampledatabase.zip>
* Ecrivez un script qui sauvegarde la base de données classicmodels. Respectez les impératifs suivants :
  * La sauvegarde de la base de données doit être contenue dans un seul fichier
  * Ce fichier doit être compressé au format .bz2
  * Le fichier doit être horodaté (année-mois-jour-heure-minutes-secondes)
  * Si la sauvegarde réussit, le script conserve uniquement les 5 fichiers de sauvegarde les plus récents
  * Ce script doit se lancer toutes les 10 minutes, les logs doivent être envoyés dans /var/log/dump-mysql.log
  * Trouvez un outil permettant de controller le volume du fichier de log /var/log/dump-mysql.log. Proposez une configuration qui vous parait raisonnable

Résultat attendu :

Les résultats doivent être disponible sur votre dépot git, dans un répertoire NVIDIA/TD-9-11-22/\<nom de l'élève>

Vous devez fournir :

* setup-mysql :
  * Un readme ou un script expliquant comment :
    * installer MySQL
    * Importer la base de données
      NB : Si vous faites un readme, vous devez indiquer les commandes utilisées
* dump-database.sh :
  * Un script de base de sauvegarde de base de données
* dump-database.service & dump-database.timer :
  * Les fichiers permettant de configurer la sauvegarde en tant que service
* setup-dump-database-service :
  * Un readme ou un script expliquant comment configurer le service. NB : Si vous faites un readme, vous devez indiquer les commandes utilisées
* setup-dump-database-logs-cleanup :
  * Un readme ou un script expliquant comment configurer le contrôle des logs

Date limite de rendu : Mercredi 23/11 18:00
