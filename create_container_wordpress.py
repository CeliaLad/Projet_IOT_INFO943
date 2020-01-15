
import time
import docker

client = docker.DockerClient(base_url='193.48.125.179:2326') #connexion serveur distant equipe de docker
client.events() #recupere les events docker



print(client.images.list()) #affiche les images disponibles

print("start containers\n")


#image = client.images.pull('wordpress') #recupere une image une
wordpress_container = client.containers.run('wordpress:4-php5.6', name="docker_wordpress", auto_remove=True, detach=True, ports={'8080/tcp':None}) #cree un container avec l'image associee
helloworld_container = client.containers.run('hello-world', auto_remove=True,detach=True)

#myWordpress = client.containers.run('wordpress', 

#Docker ps
for container in client.containers.list(): # equivalent docker ps
  print(container.id)
  print(container.name)
  print(container.image)
  print(container.ports)
  print("\n")


print("wait 10sec\n")
time.sleep(30)


print("stop containers\n")
#for container in client.containers.list():
  #container.stop()

for container in client.containers.list():
  print(container.id)

print("fin programme")