#!/bin/bash

# Dump the database to a file, and delete the file after 5 dumps.
# Sends logs to /var/log/dump-mysql.log
# WARNING ! this script must be run as root

echo "Dumping database $(date +%Y-%m-%d_%H:%M:%S)" >> /var/log/dump-mysql.log


mysqldump -u reader -p"password" --databases classicmodels > mysqldump.sql 2>> /var/log/dump-mysql.log

# compress the file to bz2, without keeping the original file

bzip2 -f mysqldump.sql >> /var/log/dump-mysql.log

# remove the old dumps from /var/backup/mysql (.save5)

rm -f /var/backups/mysql/backup*.save5 >> /var/log/dump-mysql.log

# rename the files from .save1, .save2, .save3, .save4 to .save2, .save3, .save4, .save5

for f in $(ls /var/backups/mysql/backup*.save*); do                  #iterate only one the files that are backup*.save?   -> dumps from 1 to 4
    echo "$f" >> /var/log/dump-mysql.log    # log the file name
    mv "$f" "${f::-1}$((${f: -1} + 1))"     # add 1 to the last character, keep the rest
done

# rename the file to backup_year-month-day-hour-minutes-seconds.sql.bz2.save1 and move it to /var/backups/mysql

mv mysqldump.sql.bz2 /var/backups/mysql/backup_$(date +%Y-%m-%d-%H-%M-%S).sql.bz2.save1 >> /var/log/dump-mysql.log

echo "Done" >> /var/log/dump-mysql.log
