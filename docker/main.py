import docker

client = docker.from_env()

client.images.pull('nginx')
client.images.pull('ubuntu')
client.images.pull('mysql')
