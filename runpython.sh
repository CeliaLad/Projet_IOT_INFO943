#! /bin/bash

myvariable=$(mysql -u root -pmypassword --execute="connect mysql; SELECT * FROM user;")

echo "${myvariable}"

while [ "${myvariable}" == "" ]
do
sleep 5
done

python /usr/src/app/helloworld.py