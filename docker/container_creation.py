import time
import docker

client = docker.DockerClient(base_url='193.48.125.180:2326') #connexion serveur distant equipe de docker
client.events() #recupere les events docker
liste_container = []


FOLDER_PATH = "./"
print("Building image")
client.images.build(path=FOLDER_PATH,tag="mon_image")


print("stop & remove containers\n")
for container in client.containers.list():
  container.stop()

for container in client.containers.list(all):
  container.remove()


print("Image disponible : \n")
print(client.images.list()) #affiche les images disponibles


print("start containers\n")
#image = client.images.pull('wordpress') #recupere une image une
wordpress_container = client.containers.run('eclipse-mosquitto:1.4.4', name="docker_mosquitto61", auto_remove=True, detach=True, ports={'8080/tcp':None}) #cree un container avec l'image associee
helloworld_container = client.containers.run('hello-world', auto_remove=True,detach=True)

#On fait mass container parceque : 
print("creation containers")
for i in range(10):
  print(i)
  client.containers.run('alpine:3', name="container_aaaa"+str(i), detach=True, ports={'8080/tcp':None}) #cree un container avec l'image associee



print("All containers informations:")
print client.containers.list(all)
#Docker ps : affiche les containers run
for container in client.containers.list(all): # equivalent docker ps
  print(container.id)
  print(container.name)
  print(container.image)
  print(container.ports)
  print("\n")


print("wait 10sec\n")
time.sleep(10)


print("stop containers\n")
for container in client.containers.list(all):
  container.stop()

for container in client.containers.list(all):
  print(container.id)

print("fin programme")