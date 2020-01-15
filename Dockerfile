FROM python:3

ADD docker_main.py /

RUN pip install docker

CMD [ "python", "./docker_main.py" ]
