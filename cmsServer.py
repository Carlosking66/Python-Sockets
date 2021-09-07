# Prueba de codificación de Sockets
# * Carlos Menéndez -  Sep 2021
# Módulo Server.py

import socket
import sys, errno  #  Para manejo error broken pipe
  

Host="0.0.0.0"
Port=64046

# Se crea el objeto para la conexión 
socServer=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se enlaza con los datos escogidos de Host y Port.
socServer.bind((Host, Port))
# Se le pone a escuchar.
try:
  socServer.listen(1) # 1 conex.

  print("Servidor en escucha...")
  socClient, Dir=socServer.accept() # Espera a que el cliente haga una petición y la acepta.
  print ("Conexión establecida con %s por el port: %s" %(Dir[0], Dir[1]))
# Empieza BUCLE ESTADO CONECTADO:  
  while True:
    print("Esperando a recibir datos de la máquina cliente...")
    DatosRec=socClient.recv(1024)
    Recibido=DatosRec.decode("utf-8")
    print("Datos recibidos: %s" %(Recibido))
    RespuestaServ=bytes("Servidor confirma que ha recibido sus datos...", 'utf-8')

    socClient.sendall(RespuestaServ)    
    
    if Recibido=="fin":
      
      print("Conexión finalizada por el usuario!!. Adiós!")
      
      socClient.sendall(DatosRec)
      
      break  # Sale del bucle de conexión.
except IOError as e:
  if e.errno == errno.EPIPE:
    print("Tubería rota! - Necesaria reparación del código!.")
    print ("Contact   with CMS Computing in Asturias (Spain)")
    
finally:
  socServer.close()