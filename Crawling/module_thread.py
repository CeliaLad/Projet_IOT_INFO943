# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:12:47 2020

@author: chevrons
"""
# -------- Importation des blibliothèques-----------
import json
from threading import Thread
import requests
import time as t

import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.118.41" 
list_success = []


# ------Classe thread charge wordpress--------------
class ddos_thread(Thread):
    
    def __init__(self, url, nbreRequest, time):
        Thread.__init__(self)
        self.URL = url
        self.N = nbreRequest
        self.dodo = time
        self.success = 0
        
    def run(self):
        for j in range (0, self.N):
            response = requests.get(self.URL)
            #print(type(response))
            if (str(response) == "<Response [200]>") :
                #print(response)
                list_success.append("ok")
            
            t.sleep(self.dodo)
    
# ----------Fonction spam requêtes Wordpress--------------
def module_thread(urlRef):
      
    print("Nbre de spam par thread?")
    N = input()
    print("Delay intra thread?")
    time = input()
    total_time = int(N)*int(time)
    print("La durée totale est estimée à: " + str(total_time) + "ms")
    
    start_time = t.time()
    
    urls = urlRef
    tabURL =[]
    
    with open('E:\\PROJ943\\tutorial\\quotes.json') as json_data:
        data = json.load(json_data)    
    #data_str = json.dumps(data)
    
    tampon = 0
    for i in range(0, len(data)):
        test = data[i]  
        for j in range(0,len(test["URL"])):         
            if test["URL"][j] != []:
                tampon = tampon + 1
                
    nbre_requete = tampon * int(N)
    print("Charge estimée à: " + str(nbre_requete) + " requêtes!")
    
    publish_str = "{'Time':" + str(total_time) +", 'Charge':" + str(nbre_requete) +"}"
    print(publish_str)
    
    #broker_address="iot.eclipse.org" #use external broker
    client = mqtt.Client("spam") #create new instance
    client.connect(broker_address) #connect to broker
    client.publish("spam_wordpress", publish_str)#publish
               
    #print(data_str)
    for i in range(0, len(data)):
        test = data[i]    
        #print(len(test["URL"]))
        for j in range(0,len(test["URL"])):
         
            if test["URL"][j] != []:
                var = test["URL"][j].replace("'","")
                if ('http' in var) == True:
                    tabURL.append(var)
                else:
                    tabURL.append(urls[0]+var)
    
    #print(tabURL)
  
    # ------Initialisation & lancements threads------------
    liste_thread = tabURL
    
    #print(liste_thread)
    #print(len(liste_thread))
    for i in range(0, len(tabURL)):
        liste_thread[i] = ddos_thread(tabURL[i], int(N), int(time))
    #print(liste_thread)
    #print(len(liste_thread))
    for i in range(0, len(tabURL)):
        liste_thread[i].start()
        
    for i in range(0, len(tabURL)):
        liste_thread[i].join()        
    
        #print(i)
    print("Nombre de requêtes réussies: " + str(len(list_success)) +" sur " + str(nbre_requete))
    #print(len(list_success))
    
    print("Temps d'execution :%s secondes ---" % (t.time() - start_time))
    