#!/bin/sh

        # host='163.172.97.125',
        # user='root',
        # passwd='mypassword',
        # db='kek',
        # port=6603)
# docker build -t monimage .
# Check if docker image exist
# else pull from docker*
# https://hub.docker.com/_/mysql

DIR=$1
if [ "$DIR" = "" ]; then
    # DIR=/home/etudiants/erwan/dockerTest/mysql-test/data
    echo "Please provide data directory"
    exit 1
fi
DIR=$(readlink -e $DIR)

# We can pass general cnf parameters as flags to the default image too
# Other names: #mysql \ # testimg

docker run \
--detach \
--name=test-mysql2 \
--env="MYSQL_ROOT_PASSWORD=mypassword" \
--publish 6605:3306 \
--volume=$DIR:/var/lib/mysql \
mysql \
--max-connections=200 \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci \
--general-log=1 \
--general-log-file=/var/lib/mysql/mysql-general-log.log


# New docker
# docker run -d --name=new-mysql -p 6604:3306 -v /home/etudiants/erwan/dockerTest/mysql-test/data:/var/lib/mysql mysql

# for i in "$@"
# do
# case $i in
#     -e=*|--extension=*)
#     EXTENSION="${i#*=}"
#     shift # past argument=value
#     ;;
#     -s=*|--searchpath=*)
#     SEARCHPATH="${i#*=}"
#     shift # past argument=value
#     ;;
#     -l=*|--lib=*)
#     LIBPATH="${i#*=}"
#     shift # past argument=value
#     ;;
#     --default)
#     DEFAULT=YES
#     shift # past argument with no value
#     ;;
#     *)
#           # unknown option
#     ;;
# esac
# done
