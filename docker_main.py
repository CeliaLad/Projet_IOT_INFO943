
import docker
import time


client = docker.DockerClient(base_url='193.48.125.179:2326')
client.events()

print("start containers\n")


client.images.list()


#mosquitto_container    = client.containers.run('eclipse-mosquitto', auto_remove=True, detach=True)
#nginx_container        = client.containers.run('nginx', auto_remove=True, detach=True)
#postgres_container     = client.containers.run('postgres', auto_remove=True, detach=True)
image = client.images.pull('wordpress')
wordpress_container     = client.containers.run(image, name="docker_wordpress", auto_remove=True, detach=True, ports={'8080/tcp':None})
#ubuntu_container       = client.containers.run('ubuntu', auto_remove=True, detach=True)
helloworld_container = client.containers.run('hello-world', auto_remove=True,detach=True)

#myWordpress = client.containers.run('wordpress', 

#Docker ps
for container in client.containers.list():
  print(container.id)
  print(container.name)
  print(container.image)
  print(container.ports)
  print("\n")



print("wait 10sec\n")
time.sleep(20)


print("stop containers\n")
for container in client.containers.list():
  container.stop()

for container in client.containers.list():
  print(container.id)
