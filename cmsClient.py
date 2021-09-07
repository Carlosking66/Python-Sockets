# Prueba de codificaciónn de Sockets
#  Módulo Cliente. * Carlos Menéndez - Sep 2021.

import socket
import sys, errno
Host="127.0.0.1"
Port=64046

try:  
  SockCli=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  SockCli.connect((Host, Port))
  print("Conexión establecida...")
# Empieza BUCLE ESTADO CONECTADO:  
  boolControl=True
  while boolControl:
    DatosAEnv=input("Datos con destino al servidor:")

    SockCli.send(bytes(DatosAEnv, encoding = "utf-8"))
    
    BytesRec=SockCli.recv(1024)    
    
    RespuestaFromServ=    BytesRec.decode("utf-8")
    print ("Respuesta recibida del servidor: %s" %(RespuestaFromServ))
    
    if DatosAEnv== "fin": 
      
      print("\a")
      boolControl=False   # Sale del bucle estado conectado
  print("Conexión cerrada!")
  print ("Terminación exitosa! Bye!! * CMS Computing 2021")
except IOError as e:
  if e.errno == errno.EPIPE:  
    print("Tuberia Rota! _ Necesaria reparación del código.")             
    print ("Contact   with CMS Computing in Asturias (Spain)")
finally:
  SockCli.close()