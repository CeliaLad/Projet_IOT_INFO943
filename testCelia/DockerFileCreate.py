import docker
import time

client = docker.DockerClient(base_url='tcp://193.48.125.179:2326')
client.events() #recupere les events docker
#print(client.images.list()) #affiche les images disponibles

imageMosquitto = client.images.pull('eclipse-mosquitto')


mosquitto_container = client.containers.run('eclipse-mosquitto',detach=True)

print("container ok")
print(client.containers.list())
