# -----------Creation de charge Ã  une BDD---------------------

import MySQLdb
from threading import Thread

import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.118.41" 

import time as t

# -----Classe thead charge Bdd-----------------
class ddos_thread_bdd(Thread):
    
    sql = "SELECT * FROM kekomatik"
    #"SELECT * FROM kekomatik as k LEFT OUTER JOIN KometuVeux as k2 ON k2.id = k.id"
    
    def __init__(self, name):
        Thread.__init__(self)
        self.Name = name    
    
    def run(self):
        
        try:
            paramMysql = {
            'host'   : '163.172.97.125',
            'user'   : 'root',
            'passwd' : 'mypassword',
            'db'     : 'kek',
            'port' : 6603
            }
            # On  crÃ©Ã© une conexion MySQL
            conn = MySQLdb.connect(**paramMysql)
            # On crÃ©Ã© un curseur MySQL
            cur = conn.cursor(MySQLdb.cursors.DictCursor)
            # On exÃ©cute la requÃªte SQL
            cur.execute(self.sql)
             #On rÃ©cupÃ¨re toutes les lignes du rÃ©sultat de la requÃªte
            rows = cur.fetchall()
            # On parcourt toutes les lignes
            #print (rows)
#            for row in rows:
#                # Pour rÃ©cupÃ©rer les diffÃ©rentes valeurs des diffÃ©rents champs
#                valeur1 = row['id']
#                valeur2 = row['kek']
#                valeur3 = row['str']
              
                # etc etc ...
    
        finally:
            # On ferme la connexion
            if conn:
                conn.close()

# ------Fonction spam requÃªte de la Bdd--------------------  
def module_bdd():
    
    print ("Nombre de requete?\n")
    N = input()
    publish_str = "{'NbreRequete':" + str(N) +"}"
    #broker_address="iot.eclipse.org" #use external broker
    client = mqtt.Client("spam") #create new instance
    client.connect(broker_address) #connect to broker
    client.publish("spam_bdd","publish_str")#publish
    
    start_time = t.time()
     
    tabThread = [0] * int(N)
    for i in range (0,int(N)):
        tabThread[i] = ddos_thread_bdd(i)
        
    for i in range (0,int(N)):
        tabThread[i].start()
        
    for i in range (0,int(N)):
        tabThread[i].join()
        #print(i)
    
    print("Temps d'execution :%s secondes ---" % (t.time() - start_time))
    
