docker run \
--detach \
--name=test-mysql2 \
--env="MYSQL_ROOT_PASSWORD=mypassword" \
--publish 6605:3306 \
--volume=$DIR:/var/lib/mysql \
mysql \ #mysql \ # testimg
# We can pass general cnf parameters as flags to the default image too
--max-connections=200 \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci \
--general-log=1 \
--general-log-file=/var/log/mysql/general-log.log
