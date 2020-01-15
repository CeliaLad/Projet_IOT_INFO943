import docker
import time

FOLDER_PATH = "./"

client = docker.DockerClient(base_url='193.48.125.179:2326')
client.events()

print("Building image")
client.images.build(path=FOLDER_PATH,tag="docker_appli")

print("Run image")
docker_container = client.containers.run('docker_appli', auto_remove=True,detach=True)

#Docker ps
for container in client.containers.list():
  print(container.id)
  print(container.name)
  print(container.image)
  print(container.ports)
  print("\n")

