#!/bin/sh

DIR=$1
if [ "$DIR" = "" ]; then
    # DIR=/home/etudiants/erwan/dockerTest/mysql-test/data
    echo "Please provide data directory"
    exit 1
fi
DIR=$(readlink -e $DIR)

# docker build -t monimage .

docker run \
--detach \
-t \
--name=testimage \
--env="MYSQL_ROOT_PASSWORD=mypassword" \
--publish 6604:3306 \
--volume=$DIR:/var/lib/mysql \
monimage