FROM mysql:latest
WORKDIR /usr/src/app
RUN apt update
RUN apt --assume-yes install python
COPY helloworld.py .
COPY runpython.sh /
RUN chmod +x /runpython.sh