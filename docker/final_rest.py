                
import docker
import subprocess
import requests
import paho.mqtt.client as mqtt
import time


client=docker.from_env()

bashCommand = """head -1 /proc/self/cgroup|cut -d/ -f3"""
output = subprocess.check_output(['bash','-c', bashCommand])
con_id=output[0:12]
con_id_str=con_id.decode("utf-8")
print(con_id_str)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code " + str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def on_publish(client, userdata, result):  # create function for callback
    print("data published \n")


client = mqtt.Client()
#client.username_pw_set("", "")
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

client.connect("192.168.118.41", 1883, 60)

client.subscribe("message")

while(True):
    url="http://193.48.125.180:2326/containers/"+con_id_str+"/stats?stream=False"
    requete = requests.get(url)
    page = requete.content
    print(page)
    client.publish("message",page)
    time.sleep(10)

